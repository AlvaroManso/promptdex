# Privacy

PromptDex is local-first by design.

The app stores prompts in a local SQLite database named `promptdex.db`. This file is ignored by git and should not be committed to public repositories.

PromptDex does not include:

- Accounts
- Authentication
- Telemetry
- Cloud sync
- External AI API calls
- Payment integrations

JSON backups are created locally. They may contain your prompts, so review backup files before sharing them.
