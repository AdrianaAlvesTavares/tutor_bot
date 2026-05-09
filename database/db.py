import sqlite3
import os

DB_PATH = "tutor.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r") as f:
        schema = f.read()
    with get_connection() as conn:
        conn.executescript(schema)
    print("✅ Banco de dados inicializado")

def get_user(user_id: int):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()
        return dict(row) if row else None

def upsert_user(user_id: int, username: str) -> dict:
    with get_connection() as conn:
        conn.execute(
            """INSERT OR IGNORE INTO users (user_id, username)
               VALUES (?, ?)""",
            (user_id, username)
        )
    return get_user(user_id)

def add_warn(user_id: int) -> str:
    user = get_user(user_id)
    new_count = user["warn_count"] + 1

    if new_count == 1:
        new_status = "warned"
    elif new_count == 2:
        new_status = "blocked_partial"
    else:
        new_status = "blocked"
        new_count = 3

    with get_connection() as conn:
        conn.execute(
            "UPDATE users SET warn_count = ?, status = ? WHERE user_id = ?",
            (new_count, new_status, user_id)
        )
    return new_status

def save_quiz_session(user_id: int, module_id: str, total: int, correct: int):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO quiz_sessions (user_id, module_id, total_q, correct_q)
               VALUES (?, ?, ?, ?)""",
            (user_id, module_id, total, correct)
        )