from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query, Response, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from promptdex.database import Base, make_engine, make_session_factory, session_dependency
from promptdex.models import Prompt, utc_now
from promptdex.schemas import (
    CATEGORIES,
    BackupExport,
    BackupImport,
    ImportResult,
    PromptBackup,
    PromptCreate,
    PromptRead,
    PromptUpdate,
)
from promptdex.seed_library import LIBRARY_VERSION_TAG, builtin_prompt_library

DEFAULT_DATABASE_URL = "sqlite:///./promptdex.db"
STATIC_DIR = Path(__file__).parent / "static"


def create_app(database_url: str = DEFAULT_DATABASE_URL, *, seed_library: bool = True) -> FastAPI:
    engine = make_engine(database_url)
    session_factory = make_session_factory(engine)
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="PromptDex", version="0.1.0")
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

    if seed_library:
        with session_factory() as session:
            if not session.scalars(select(Prompt.id).limit(1)).first():
                _seed_builtin_library(session)

    def get_session():
        yield from session_dependency(session_factory)

    @app.get("/", include_in_schema=False)
    def index() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    @app.get("/api/categories")
    def categories() -> list[str]:
        return CATEGORIES

    @app.get("/api/prompts", response_model=list[PromptRead])
    def list_prompts(
        session: Session = Depends(get_session),
        search: str | None = Query(default=None),
        category: str | None = Query(default=None),
        tag: str | None = Query(default=None),
        favorite: bool | None = Query(default=None),
        sort: str = Query(default="created_asc"),
    ) -> Sequence[Prompt]:
        prompts = session.scalars(select(Prompt).order_by(Prompt.id.asc())).all()
        filtered = [
            prompt
            for prompt in prompts
            if _matches_filters(
                prompt,
                search=search,
                category=category,
                tag=tag,
                favorite=favorite,
            )
        ]
        return _sort_prompts(filtered, sort)

    @app.post("/api/prompts", response_model=PromptRead, status_code=status.HTTP_201_CREATED)
    def create_prompt(payload: PromptCreate, session: Session = Depends(get_session)) -> Prompt:
        prompt = Prompt(**payload.model_dump())
        session.add(prompt)
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.get("/api/prompts/{prompt_id}", response_model=PromptRead)
    def get_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Prompt:
        return _get_prompt_or_404(session, prompt_id)

    @app.put("/api/prompts/{prompt_id}", response_model=PromptRead)
    def update_prompt(
        prompt_id: int,
        payload: PromptUpdate,
        session: Session = Depends(get_session),
    ) -> Prompt:
        prompt = _get_prompt_or_404(session, prompt_id)
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(prompt, field, value)
        prompt.updated_at = utc_now()
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.post("/api/prompts/{prompt_id}/use", response_model=PromptRead)
    def use_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Prompt:
        prompt = _get_prompt_or_404(session, prompt_id)
        now = utc_now()
        prompt.last_used_at = now
        prompt.updated_at = now
        session.commit()
        session.refresh(prompt)
        return prompt

    @app.post(
        "/api/prompts/{prompt_id}/duplicate",
        response_model=PromptRead,
        status_code=status.HTTP_201_CREATED,
    )
    def duplicate_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Prompt:
        prompt = _get_prompt_or_404(session, prompt_id)
        duplicate = Prompt(
            title=f"{prompt.title} (copy)",
            body=prompt.body,
            category=prompt.category,
            tags=list(prompt.tags),
            rating=prompt.rating,
            favorite=False,
        )
        session.add(duplicate)
        session.commit()
        session.refresh(duplicate)
        return duplicate

    @app.delete("/api/prompts/{prompt_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_prompt(prompt_id: int, session: Session = Depends(get_session)) -> Response:
        prompt = _get_prompt_or_404(session, prompt_id)
        session.delete(prompt)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @app.get("/api/backup/export", response_model=BackupExport)
    def export_backup(session: Session = Depends(get_session)) -> BackupExport:
        prompts = session.scalars(select(Prompt).order_by(Prompt.id.asc())).all()
        return BackupExport(
            exported_at=utc_now(),
            prompts=[_prompt_to_backup(prompt) for prompt in prompts],
        )

    @app.post(
        "/api/backup/import", response_model=ImportResult, status_code=status.HTTP_201_CREATED
    )
    def import_backup(
        payload: BackupImport, session: Session = Depends(get_session)
    ) -> ImportResult:
        if payload.replace:
            session.execute(delete(Prompt))

        imported = 0
        for backup_prompt in payload.prompts:
            session.add(_backup_to_prompt(backup_prompt))
            imported += 1

        session.commit()
        return ImportResult(imported=imported, total=len(payload.prompts))

    @app.post("/api/library/seed", response_model=ImportResult, status_code=status.HTTP_201_CREATED)
    def seed_prompt_library(session: Session = Depends(get_session)) -> ImportResult:
        imported = _seed_builtin_library(session)
        return ImportResult(
            imported=imported,
            skipped=len(builtin_prompt_library()) - imported,
            total=len(builtin_prompt_library()),
        )

    return app


def _get_prompt_or_404(session: Session, prompt_id: int) -> Prompt:
    prompt = session.get(Prompt, prompt_id)
    if prompt is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prompt not found")
    return prompt


def _matches_filters(
    prompt: Prompt,
    *,
    search: str | None,
    category: str | None,
    tag: str | None,
    favorite: bool | None,
) -> bool:
    if favorite is not None and prompt.favorite is not favorite:
        return False

    if category and prompt.category.lower() != category.strip().lower():
        return False

    tags = [item.lower() for item in prompt.tags]
    if tag and tag.strip().lower() not in tags:
        return False

    if search:
        needle = search.strip().lower()
        haystack = " ".join([prompt.title, prompt.body, prompt.category, *prompt.tags]).lower()
        if needle not in haystack:
            return False

    return True


def _sort_prompts(prompts: Sequence[Prompt], sort: str) -> list[Prompt]:
    if sort == "rating_desc":
        return sorted(prompts, key=lambda prompt: (prompt.rating, prompt.id), reverse=True)
    if sort == "favorite_desc":
        return sorted(prompts, key=lambda prompt: (prompt.favorite, prompt.id), reverse=True)
    if sort == "updated_desc":
        return sorted(prompts, key=lambda prompt: (prompt.updated_at, prompt.id), reverse=True)
    if sort == "last_used_desc":
        return sorted(
            prompts,
            key=lambda prompt: (prompt.last_used_at is not None, prompt.last_used_at, prompt.id),
            reverse=True,
        )
    if sort == "created_desc":
        return sorted(prompts, key=lambda prompt: (prompt.created_at, prompt.id), reverse=True)
    return list(prompts)


def _prompt_to_backup(prompt: Prompt) -> PromptBackup:
    return PromptBackup(
        title=prompt.title,
        body=prompt.body,
        category=prompt.category,
        tags=list(prompt.tags),
        rating=prompt.rating,
        favorite=prompt.favorite,
        created_at=prompt.created_at,
        updated_at=prompt.updated_at,
        last_used_at=prompt.last_used_at,
    )


def _backup_to_prompt(backup_prompt: PromptBackup) -> Prompt:
    now = utc_now()
    return Prompt(
        title=backup_prompt.title,
        body=backup_prompt.body,
        category=backup_prompt.category,
        tags=backup_prompt.tags,
        rating=backup_prompt.rating,
        favorite=backup_prompt.favorite,
        created_at=backup_prompt.created_at or now,
        updated_at=backup_prompt.updated_at or now,
        last_used_at=backup_prompt.last_used_at,
    )


def _seed_builtin_library(session: Session) -> int:
    existing_titles = {
        prompt.title
        for prompt in session.scalars(select(Prompt)).all()
        if LIBRARY_VERSION_TAG in prompt.tags
    }
    imported = 0

    for prompt in builtin_prompt_library():
        if prompt.title in existing_titles:
            continue
        session.add(Prompt(**prompt.model_dump()))
        imported += 1

    session.commit()
    return imported


app = create_app()
