import sqlite3
from datetime import datetime

DB_PATH = "memory/user_memory.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        content TEXT,
        image_path TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()



def store_memory(memory_type: str, content: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO memory (type, content, timestamp)
    VALUES (?, ?, ?)
    """, (memory_type, content, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def retrieve_memories(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, content, image_path FROM memory
    ORDER BY timestamp DESC
    LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def store_image_memory(memory_type: str, description: str, image_path: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO memory (type, content, image_path, timestamp)
    VALUES (?, ?, ?, ?)
    """, (memory_type, description, image_path, datetime.now().isoformat()))

    conn.commit()
    conn.close()

