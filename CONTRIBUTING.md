# Contributing to PromptDex

Thanks for helping improve PromptDex.

## Principles

- Keep it local-first.
- Do not add authentication, cloud sync, telemetry, payments, or external AI API calls.
- Prefer simple Python, FastAPI, SQLite, and vanilla frontend code.
- Keep the app useful for people who just want to run it locally.

## Setup

```powershell
uv sync
uv run uvicorn promptdex.main:app --reload --host 127.0.0.1 --port 8000
```

## Checks

Before opening a PR, run:

```powershell
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Prompt Library Contributions

Built-in prompts should be:

- Useful without private context
- Bilingual when practical
- Clear about expected output
- Free of API keys, customer data, emails, phone numbers, or proprietary content
