# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server (port 5001, debug mode)
python expense-tracker/app.py

# Run tests
pytest

# Run a single test file
pytest tests/test_auth.py
```

No linter is currently configured.

## Architecture

**Spendly** is a Flask web application for personal expense tracking (Indian Rupees). It uses a traditional server-side rendering pattern:

- **`expense-tracker/app.py`** — All Flask routes and application logic. The app runs on port 5001 with debug mode enabled.
- **`expense-tracker/database/db.py`** — SQLite database helpers (`get_db`, `init_db`, `seed_db`). Currently stubbed out for implementation.
- **`expense-tracker/templates/`** — Jinja2 templates. `base.html` is the layout with navbar and footer; all other templates extend it.
- **`expense-tracker/static/css/`** — `style.css` defines the global design system (CSS variables, components); `landing.css` is page-specific.
- **`expense-tracker/static/js/main.js`** — Vanilla JS entry point, currently a stub.

## Routing Pattern

All routes are defined with `@app.route()` in `app.py`. Currently implemented routes are GET-only (landing, register, login, terms, privacy). POST handlers and authenticated routes are stubbed with placeholder returns, each labeled with the curriculum step that implements them (Steps 3–9).

## Database

SQLite with `row_factory = sqlite3.Row` and foreign keys enabled. The database file (`expense_tracker.db`) is gitignored. `init_db()` should use `CREATE TABLE IF NOT EXISTS`. Connection is obtained per-request via `get_db()`.

## Design System

CSS custom properties are defined in `:root` in `style.css`:
- Primary: `#1a472a` (dark green), Accent: `#c17f24` (gold)
- Fonts: DM Serif Display (headings), DM Sans (body) — loaded from Google Fonts in `base.html`

## Project Context

This is a scaffolded teaching project. The frontend (landing page, auth forms, legal pages) is complete. The backend features — database setup, authentication, and expense CRUD — are stubs to be implemented through a 9-step curriculum. When extending the app, follow the existing step comments in `app.py` for the intended implementation order.
