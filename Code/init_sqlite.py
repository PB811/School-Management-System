"""
One-time setup script: creates sms.db with all required tables and a default admin user.
Run once before launching the app:
    uv run init_sqlite.py

Can also be imported and called as init_db() from Run.py for frozen EXE auto-init.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sms.db")


def init_db(db_path=None):
    """Create DB and tables if they don't already exist. Safe to call multiple times."""
    path = db_path or DB_PATH
    if os.path.exists(path):
        return  # Already initialised

    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.executescript("""
CREATE TABLE IF NOT EXISTS users (
    Staff_ID    INTEGER,
    Username    TEXT,
    Password    TEXT,
    First_Name  TEXT,
    Last_Name   TEXT
);

CREATE TABLE IF NOT EXISTS students (
    Registration_Number INTEGER,
    First_Name          TEXT,
    Last_Name           TEXT,
    Gender              TEXT,
    Age                 INTEGER,
    Address             TEXT,
    Contact             TEXT,
    Email_ID            TEXT,
    Grade               TEXT,
    Section             TEXT
);

CREATE TABLE IF NOT EXISTS teachers (
    Staff_ID    INTEGER,
    First_Name  TEXT,
    Last_Name   TEXT,
    Gender      TEXT,
    Age         INTEGER,
    Designation TEXT,
    Address     TEXT,
    Contact     TEXT,
    Email_ID    TEXT
);

CREATE TABLE IF NOT EXISTS staff (
    Staff_ID    INTEGER,
    First_Name  TEXT,
    Last_Name   TEXT,
    Gender      TEXT,
    Age         INTEGER,
    Designation TEXT,
    Address     TEXT,
    Contact     TEXT,
    Email_ID    TEXT
);

CREATE TABLE IF NOT EXISTS subjects (
    Subject_ID  INTEGER,
    Subject     TEXT
);
""")

    # Seed a default admin user so you can log in immediately.
    # Username: admin   Password: admin
    cur.execute("SELECT COUNT(*) FROM users WHERE Username = 'admin'")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO users (Staff_ID, Username, Password, First_Name, Last_Name) VALUES (?, ?, ?, ?, ?)",
            (1, "admin", "admin", "Admin", "User"),
        )
        print("Default user created — Username: admin  Password: admin")
    else:
        print("Default user already exists.")

    conn.commit()
    conn.close()

    print(f"Database initialised at: {path}")


if __name__ == "__main__":
    init_db()
