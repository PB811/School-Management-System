"""
mysql.connector compatibility shim — routes to SQLite.
Drop this file at Code/mysql/connector.py so that
`import mysql.connector` resolves here instead of the real package.
"""
import sqlite3
import re
import os

# sms.db lives in Code/ (two levels up from Code/mysql/connector.py)
_DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sms.db")

# Single persistent connection shared across all modules
_conn = None


def _get_conn():
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = None  # return plain tuples (matches mysql behaviour)
    return _conn


class _Cursor:
    def __init__(self, conn):
        self._conn = conn
        self._cur = conn.cursor()

    def execute(self, query, params=None):
        # Skip USE <db> statements — not meaningful for SQLite
        if query.strip().lower().startswith("use "):
            return
        # MySQL uses %s placeholders; SQLite uses ?
        query = re.sub(r"%s", "?", query)
        if params is not None:
            self._cur.execute(query, params)
        else:
            self._cur.execute(query)

    def fetchall(self):
        return self._cur.fetchall()

    def fetchone(self):
        return self._cur.fetchone()

    @property
    def lastrowid(self):
        return self._cur.lastrowid


class _Connection:
    def __init__(self):
        self._conn = _get_conn()

    def is_connected(self):
        return True

    def cursor(self):
        return _Cursor(self._conn)

    def commit(self):
        self._conn.commit()

    def close(self):
        # No-op: keep the underlying SQLite connection alive.
        # The existing code calls close() immediately after getting a cursor
        # and then reconnects inside each method — we just reuse one connection.
        pass


def connect(**kwargs):
    """Mimics mysql.connector.connect(); all kwargs (host, user, password) ignored."""
    return _Connection()


# Expose the Error class so any `except mysql.connector.Error` blocks work
class Error(Exception):
    pass
