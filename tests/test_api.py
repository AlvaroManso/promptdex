from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from promptdex.main import create_app


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    app = create_app(f"sqlite:///{tmp_path / 'promptdex.db'}", seed_library=False)
    with TestClient(app) as test_client:
        yield test_client


def create_prompt(client: TestClient, **overrides: object) -> dict:
    payload = {
        "title": "Refactor buddy",
        "body": "Help me refactor this Python module without changing behavior.",
        "category": "Coding",
        "tags": ["python", "codex"],
        "rating": 4,
        "favorite": False,
    }
    payload.update(overrides)

    response = client.post("/api/prompts", json=payload)

    assert response.status_code == 201
    return response.json()


def test_create_and_list_prompts(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.get("/api/prompts")

    assert response.status_code == 200
    assert response.json() == [prompt]
    assert prompt["id"] == 1
    assert prompt["tags"] == ["python", "codex"]
    assert prompt["created_at"]
    assert prompt["updated_at"]
    assert prompt["last_used_at"] is None


def test_search_category_and_tag_filters(client: TestClient) -> None:
    create_prompt(client, title="Debug crash", category="Debugging", tags=["errors", "python"])
    create_prompt(client, title="Launch email", category="Marketing", tags=["copy", "campaign"])

    search_response = client.get("/api/prompts", params={"search": "crash"})
    category_response = client.get("/api/prompts", params={"category": "Marketing"})
    tag_response = client.get("/api/prompts", params={"tag": "python"})

    assert [prompt["title"] for prompt in search_response.json()] == ["Debug crash"]
    assert [prompt["title"] for prompt in category_response.json()] == ["Launch email"]
    assert [prompt["title"] for prompt in tag_response.json()] == ["Debug crash"]


def test_update_favorite_and_rating(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.put(
        f"/api/prompts/{prompt['id']}",
        json={"favorite": True, "rating": 5, "tags": ["python", "keeper"]},
    )

    assert response.status_code == 200
    updated = response.json()
    assert updated["favorite"] is True
    assert updated["rating"] == 5
    assert updated["tags"] == ["python", "keeper"]


def test_use_prompt_sets_last_used_at_and_returns_body(client: TestClient) -> None:
    prompt = create_prompt(client, body="Copy exactly this useful prompt.")

    response = client.post(f"/api/prompts/{prompt['id']}/use")

    assert response.status_code == 200
    used = response.json()
    assert used["body"] == "Copy exactly this useful prompt."
    assert used["last_used_at"] is not None


def test_delete_prompt(client: TestClient) -> None:
    prompt = create_prompt(client)

    response = client.delete(f"/api/prompts/{prompt['id']}")

    assert response.status_code == 204
    assert client.get("/api/prompts").json() == []


def test_sort_prompts_by_rating_favorite_updated_and_last_used(client: TestClient) -> None:
    low = create_prompt(client, title="Low value", rating=2, favorite=False)
    high = create_prompt(client, title="High value", rating=5, favorite=True)

    rating_response = client.get("/api/prompts", params={"sort": "rating_desc"})
    favorite_response = client.get("/api/prompts", params={"sort": "favorite_desc"})

    client.put(f"/api/prompts/{low['id']}", json={"title": "Recently updated"})
    updated_response = client.get("/api/prompts", params={"sort": "updated_desc"})

    client.post(f"/api/prompts/{high['id']}/use")
    last_used_response = client.get("/api/prompts", params={"sort": "last_used_desc"})

    assert [prompt["title"] for prompt in rating_response.json()] == ["High value", "Low value"]
    assert [prompt["title"] for prompt in favorite_response.json()] == ["High value", "Low value"]
    assert updated_response.json()[0]["title"] == "Recently updated"
    assert last_used_response.json()[0]["title"] == "High value"


def test_duplicate_prompt_creates_editable_copy(client: TestClient) -> None:
    prompt = create_prompt(client, title="Research sprint", tags=["research", "en"])

    response = client.post(f"/api/prompts/{prompt['id']}/duplicate")

    assert response.status_code == 201
    duplicate = response.json()
    assert duplicate["id"] != prompt["id"]
    assert duplicate["title"] == "Research sprint (copy)"
    assert duplicate["body"] == prompt["body"]
    assert duplicate["tags"] == ["research", "en"]
    assert duplicate["last_used_at"] is None


def test_export_and_import_json_backup(client: TestClient, tmp_path: Path) -> None:
    create_prompt(client, title="Backup me", tags=["backup", "es"], favorite=True)

    export_response = client.get("/api/backup/export")
    backup = export_response.json()

    assert export_response.status_code == 200
    assert backup["version"] == 1
    assert backup["prompts"][0]["title"] == "Backup me"

    import_app = create_app(f"sqlite:///{tmp_path / 'imported.db'}", seed_library=False)
    with TestClient(import_app) as import_client:
        import_response = import_client.post("/api/backup/import", json=backup)

        assert import_response.status_code == 201
        assert import_response.json()["imported"] == 1
        assert import_client.get("/api/prompts").json()[0]["title"] == "Backup me"


def test_seed_library_loads_bilingual_prompts_once(client: TestClient) -> None:
    first_response = client.post("/api/library/seed")
    second_response = client.post("/api/library/seed")

    prompts = client.get("/api/prompts").json()
    tags = {tag for prompt in prompts for tag in prompt["tags"]}

    assert first_response.status_code == 201
    assert first_response.json()["imported"] >= 20
    assert second_response.json()["imported"] == 0
    assert {"es", "en", "library-2026-05"}.issubset(tags)
