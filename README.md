# PromptDex

PromptDex is a local-first Pokédex of prompts for storing, searching, rating, favoriting, and copying AI prompts. It runs on your machine with FastAPI, SQLite, SQLAlchemy, and a simple HTML/CSS/JS frontend.

## Features

- Create, edit, and delete prompts
- Search by title, body, category, or tag
- Filter by category, tag, and favorites
- Mark prompts as favorites
- Rate prompts from 1 to 5 stars
- Copy prompt text to the clipboard
- Track the last used date when a prompt is copied
- Duplicate useful prompts
- Sort by newest, rating, favorites, updated, and last used
- Export and import JSON backups
- Seed a bilingual Spanish/English prompt library curated for May 2026 workflows
- Persist data locally in SQLite

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

## Run Locally

```powershell
uv sync
uv run uvicorn promptdex.main:app --reload --host 127.0.0.1 --port 8000
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

Prompt data is stored in `promptdex.db` in the project root by default.

The app auto-loads the built-in bilingual prompt library when a fresh database is empty. You can also press `Biblioteca ES/EN` in the UI to load any missing built-in prompts.

## Shortcuts

- `Ctrl+S` / `Cmd+S`: save the current form
- `Ctrl+K` / `Cmd+K`: focus search
- `Ctrl+Shift+C` / `Cmd+Shift+C`: copy the first visible prompt
- `/`: focus search when you are not typing in a field

## Development

Run tests:

```powershell
uv run pytest
```

Run linting:

```powershell
uv run ruff check .
```

Format code:

```powershell
uv run ruff format .
```

## API

- `GET /api/prompts`
- `POST /api/prompts`
- `GET /api/prompts/{id}`
- `PUT /api/prompts/{id}`
- `DELETE /api/prompts/{id}`
- `POST /api/prompts/{id}/use`
- `POST /api/prompts/{id}/duplicate`
- `GET /api/categories`
- `GET /api/backup/export`
- `POST /api/backup/import`
- `POST /api/library/seed`
