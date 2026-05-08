# Spec: Registration

## Overview
This step implements user registration, login, logout, and session-based
authentication for Spendly. After this step, users can create an account,
sign in, and access protected pages. Unauthenticated users are redirected
to `/login`. The backend routes for this step are already implemented in
`app.py` — this spec documents what exists and what still needs verification
before the step can be marked complete.

## Depends on
Step 1 — Database Setup (users table must exist).

## Routes
All routes are already implemented in `app.py`:

- `GET  /register` — render registration form — public
- `POST /register` — create account, redirect to `/login` on success — public
- `GET  /login` — render login form — public
- `POST /login` — validate credentials, set session, redirect to `/dashboard` — public
- `GET  /logout` — clear session, redirect to `/login` — public
- `GET  /dashboard` — protected landing page after login — logged-in only

## Database changes
No database changes — `users` table already defined in Step 1.

## Templates
- **Create:** none (templates already exist from frontend scaffold)
- **Modify:**
  - `register.html` — form must have `name`, `email`, `password` fields;
    must display `{{ error }}` when passed from the route
  - `login.html` — form must have `email`, `password` fields;
    must display `{{ error }}` when passed from the route
  - `dashboard.html` — must accept and display `user_name` variable;
    must include a logout link pointing to `/logout`

## Files to change
- `expense-tracker/templates/register.html` — verify form field names and error display
- `expense-tracker/templates/login.html` — verify form field names and error display
- `expense-tracker/templates/dashboard.html` — verify user_name display and logout link

## Files to create
No new files.

## New dependencies
No new dependencies — `werkzeug.security` already installed.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only — no string formatting in SQL
- Passwords hashed with `werkzeug.security.generate_password_hash`
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Use `session["user_id"]` and `session["user_name"]` as the session keys
- `login_required` decorator already defined in `app.py` — use it on all protected routes

## Definition of done
- [ ] Visiting `/register` shows the registration form
- [ ] Submitting the form with valid data creates a user in the DB and redirects to `/login`
- [ ] Submitting with a duplicate email shows an error message on the page
- [ ] Submitting with a missing field shows "All fields are required."
- [ ] Submitting with a password under 8 chars shows the length error
- [ ] Visiting `/login` shows the login form
- [ ] Logging in with valid credentials sets the session and redirects to `/dashboard`
- [ ] Logging in with wrong credentials shows "Invalid email or password."
- [ ] `/dashboard` displays the logged-in user's name
- [ ] `/dashboard` has a working logout link
- [ ] Visiting `/dashboard` while logged out redirects to `/login`
- [ ] Logging out clears the session and redirects to `/login`
