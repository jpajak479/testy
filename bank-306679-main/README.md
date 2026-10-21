# Bank application – {{STUDENT}} (album {{ALBUM}})

Automated Testing course, University of Gdańsk.

A project developed step by step during the course. You write the code and the tests yourself.

## Running the tests

```bash
python3 -m venv .venv             # once per repository
source .venv/bin/activate         # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest
```

Why a virtual environment: newer systems (e.g. Homebrew on macOS) refuse `pip install` into the system Python (`externally-managed-environment`). The venv keeps this project's libraries separate. Activate it in every new terminal.

## Structure

| Path | Purpose |
|---|---|
| `src/` | application code (`src/account.py` is an empty skeleton you fill in) |
| `tests/unit/` | unit tests (pytest); `test_account.py` has the first test, which fails until you implement it |
| `.github/workflows/tests.yml` | CI: tests run on every push and pull request |
| `pytest.ini` | pytest configuration |

## Files for AI agents

| File | For whom | What it does |
|---|---|---|
| `AGENTS.md` | most AI tools | rules: the agent only reviews, it does not write code |
| `CLAUDE.md` | Claude Code | loads `AGENTS.md` |
| `GEMINI.md` | Gemini CLI | loads `AGENTS.md` |

In class, AI is used for code review only. You write the code and the tests yourself.

## Workflow

1. A new branch from `main` for every feature.
2. Test → minimal implementation → refactor → commit.
3. Push and open a pull request; merge once CI is green.
