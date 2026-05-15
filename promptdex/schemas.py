from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

CATEGORIES = [
    "Coding",
    "Debugging",
    "Architecture",
    "Design",
    "Marketing",
    "Productivity",
    "Research",
    "Agents",
    "Prompts for Codex",
    "Prompts for Claude",
    "Prompts for ChatGPT",
]


class PromptCreate(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    body: str = Field(min_length=1)
    category: str = Field(default="Coding", min_length=1, max_length=80)
    tags: list[str] = Field(default_factory=list)
    rating: int = Field(default=3, ge=1, le=5)
    favorite: bool = False

    @field_validator("title", "body", "category")
    @classmethod
    def strip_required_text(cls, value: str) -> str:
        stripped = value.strip()
        if not stripped:
            raise ValueError("Value cannot be blank.")
        return stripped

    @field_validator("tags")
    @classmethod
    def normalize_tags(cls, value: list[str]) -> list[str]:
        seen: set[str] = set()
        normalized: list[str] = []
        for tag in value:
            cleaned = tag.strip().lower()
            if cleaned and cleaned not in seen:
                seen.add(cleaned)
                normalized.append(cleaned)
        return normalized


class PromptUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=160)
    body: str | None = Field(default=None, min_length=1)
    category: str | None = Field(default=None, min_length=1, max_length=80)
    tags: list[str] | None = None
    rating: int | None = Field(default=None, ge=1, le=5)
    favorite: bool | None = None

    @field_validator("title", "body", "category")
    @classmethod
    def strip_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return value
        stripped = value.strip()
        if not stripped:
            raise ValueError("Value cannot be blank.")
        return stripped

    @field_validator("tags")
    @classmethod
    def normalize_optional_tags(cls, value: list[str] | None) -> list[str] | None:
        if value is None:
            return value
        return PromptCreate.normalize_tags(value)


class PromptRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    body: str
    category: str
    tags: list[str]
    rating: int
    favorite: bool
    created_at: datetime
    updated_at: datetime
    last_used_at: datetime | None


class PromptBackup(BaseModel):
    title: str = Field(min_length=1, max_length=160)
    body: str = Field(min_length=1)
    category: str = Field(min_length=1, max_length=80)
    tags: list[str] = Field(default_factory=list)
    rating: int = Field(default=3, ge=1, le=5)
    favorite: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None
    last_used_at: datetime | None = None

    @field_validator("title", "body", "category")
    @classmethod
    def strip_backup_text(cls, value: str) -> str:
        return PromptCreate.strip_required_text(value)

    @field_validator("tags")
    @classmethod
    def normalize_backup_tags(cls, value: list[str]) -> list[str]:
        return PromptCreate.normalize_tags(value)


class BackupExport(BaseModel):
    version: Literal[1] = 1
    exported_at: datetime
    prompts: list[PromptBackup]


class BackupImport(BaseModel):
    version: Literal[1] = 1
    replace: bool = False
    prompts: list[PromptBackup]


class ImportResult(BaseModel):
    imported: int
    skipped: int = 0
    total: int
