import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "expense_tracker.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                name          TEXT    NOT NULL,
                email         TEXT    NOT NULL UNIQUE,
                password_hash TEXT    NOT NULL,
                created_at    TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS expenses (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                amount      REAL    NOT NULL,
                category    TEXT    NOT NULL,
                date        TEXT    NOT NULL,
                description TEXT,
                created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
            );
        """)


def seed_db():
    with get_db() as db:
        if db.execute("SELECT id FROM users LIMIT 1").fetchone():
            return
        db.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
        )
        user_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
        db.executemany(
            "INSERT INTO expenses (user_id, amount, category, date, description)"
            " VALUES (?, ?, ?, ?, ?)",
            [
                (user_id, 450.00,  "Food",          "2026-05-01", "Lunch at Sharma Dhaba"),
                (user_id, 1200.00, "Transport",     "2026-05-01", "Monthly metro pass"),
                (user_id, 2500.00, "Shopping",      "2026-05-03", "New earphones"),
                (user_id, 800.00,  "Bills",         "2026-05-04", "Electricity bill"),
                (user_id, 350.00,  "Food",          "2026-05-05", "Groceries"),
                (user_id, 600.00,  "Health",        "2026-05-06", "Pharmacy"),
                (user_id, 999.00,  "Entertainment", "2026-05-06", "Netflix subscription"),
                (user_id, 1500.00, "Other",         "2026-05-07", "Miscellaneous"),
            ],
        )
