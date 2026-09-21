import os
import aiosqlite

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "users.db"
)

DEFAULT_LENGTH = 12


async def init_db() -> None:
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                password_length INTEGER NOT NULL
            )
            """
        )
        await db.commit()


async def get_setting(user_id: int) -> int:
    """Return the saved password length for a user, or the default."""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT password_length FROM users WHERE user_id = ?", (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else DEFAULT_LENGTH


async def set_setting(user_id: int, password_length: int) -> None:
    """Insert or update the password length for a user."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO users (user_id, password_length)
            VALUES (?, ?)
            ON CONFLICT(user_id) DO UPDATE SET password_length = excluded.password_length
            """,
            (user_id, password_length),
        )
        await db.commit()