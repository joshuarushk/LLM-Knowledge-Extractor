import sqlite3
from .base import Step

DB_FILE = "analysis.db"

class StorageStep(Step):
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        cur = self.conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            summary TEXT,
            topics TEXT,
            sentiment TEXT,
            keywords TEXT,
            raw_text TEXT
        )
        """)
        self.conn.commit()

    def run(self, data: dict) -> dict:
        cur = self.conn.cursor()
        cur.execute("""
        INSERT INTO analyses (title, summary, topics, sentiment, keywords, raw_text)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data.get("title"),
            data.get("summary"),
            ",".join(data.get("topics", [])),
            data.get("sentiment"),
            ",".join(data.get("keywords", [])),
            data.get("text")
        ))
        self.conn.commit()
        data["id"] = cur.lastrowid 
        return data
