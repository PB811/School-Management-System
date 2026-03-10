# School Management System

A desktop School Management System built with **Python + PyQt5**, created as a school project by me. I made this in school, so it may not follow all the best practices, infact it doesn't follow any best practice. I just managed to get this done:)

![Python](https://img.shields.io/badge/Python-3.12-blue) ![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green) ![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey) ![Platform](https://img.shields.io/badge/Platform-Windows-blue)

---

## Features

- Student, Teacher, Staff, and Subject management (full CRUD)
- User authentication (login / sign-up)
- Search and filter records in table views
- Qt-based dark-themed GUI with image assets
- Standalone Windows EXE — no Python installation needed on target machine

---

## Screenshots

See [`Snipets of Outputs/`](Snipets%20of%20Outputs/) for screenshots of the running app.

---

## Quick Start

### Prerequisites

- [uv](https://github.com/astral-sh/uv) package manager
- Python 3.12

### Run from source

```bash
cd Code
uv sync
uv run init_sqlite.py   # first time only — creates the database
uv run SSC.py
```

Default login: **admin / admin**

---

## Project Structure

```
School Management System/
├── Run.py                        # Root launcher
├── SchoolMS.spec                 # PyInstaller build spec
├── Code/
│   ├── SSC.py                    # Splash screen (entry point)
│   ├── LOGIN_PAGE.py             # Login window
│   ├── SIGN_UP_PAGE.py           # Registration
│   ├── SMS_MAIN_INTERFACE.py     # Main dashboard
│   ├── init_sqlite.py            # DB initialiser (SQLite)
│   ├── mysql/                    # mysql.connector compatibility shim (uses SQLite)
│   ├── QRC_FILES/                # Compiled Qt resource modules + raw images
│   ├── *.py                      # Feature windows (Add/Manage/Update)
│   ├── *.ui                      # Qt Designer source files
│   └── pyproject.toml
├── Forms/                        # Plain-text form layout notes
├── Flowcharts/                   # App flowchart images
└── Snipets of Outputs/           # Screenshots
```

---

## Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Language  | Python 3.12                       |
| GUI       | PyQt5 (Qt Designer `.ui` files)   |
| Database  | SQLite via `mysql.connector` shim |
| Packaging | PyInstaller (Windows EXE)         |
| Env mgmt  | [uv](https://github.com/astral-sh/uv) |

---

## Build Windows EXE

```bash
# Install PyInstaller (one-time)
cd Code
uv add --dev pyinstaller

# Build from project root
cd ..
uv run --project Code pyinstaller SchoolMS.spec
```

Output: `dist/SchoolMS/SchoolMS.exe`

The EXE creates the database automatically on first run. No Python required on the target machine.

---

## Application Flow

```
SSC (Splash Screen)
  └─► Login
        └─► Main Dashboard
              ├─► Students   (Add / Manage / Update)
              ├─► Teachers   (Add / Manage / Update)
              ├─► Staff      (Add / Manage / Update)
              ├─► Users      (Add / Manage / Update)
              └─► Subjects   (Create / Manage / Update)
```

---

## License

School project — for educational use.
