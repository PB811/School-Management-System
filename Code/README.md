# School Management System

A desktop School Management System built with **Python + PyQt5 + SQLite**, created as a school project.

---

## Quick Start (Development)

### Prerequisites
- [uv](https://github.com/astral-sh/uv) package manager
- Python 3.12

### Run the app

```bash
cd Code
uv sync
uv run init_sqlite.py   # first time only — creates sms.db
uv run SSC.py
```

Default login: **admin / admin**

---

## Run from project root

```bash
# Windows
uv run --project Code python Run.py

# Or use the batch file
launch.bat
```

---

## Build Windows EXE (PyInstaller)

```bash
# From project root
uv add --dev pyinstaller --project Code
pyinstaller SchoolMS.spec
```

Output: `dist/SchoolMS/SchoolMS.exe`

> The EXE auto-creates `sms.db` on first run. No Python needed on the target machine.

---

## Docker (Linux / WSL2 with X11)

```bash
# Allow Docker to connect to your display
xhost +local:docker

# Build and run
docker-compose up
```

### Windows (XLaunch)

1. Install and start [VcXsrv](https://sourceforge.net/projects/vcxsrv/) (XLaunch)
2. Run:
   ```cmd
   set DISPLAY=host.docker.internal:0
   docker-compose up
   ```

---

## Project Structure

```
Code/
├── SSC.py                    # Splash screen (entry point)
├── LOGIN_PAGE.py             # Login window
├── SIGN_UP_PAGE.py           # Registration
├── SMS_MAIN_INTERFACE.py     # Main dashboard
├── init_sqlite.py            # DB init (SQLite)
├── Initialization.py         # DB init (MySQL — legacy)
├── mysql/                    # SQLite shim (replaces mysql.connector)
├── QRC_FILES/                # Compiled Qt resource modules
├── *.ui                      # Qt Designer source files
└── pyproject.toml
```

---

## Database

Uses **SQLite** (`Code/sms.db`) via a `mysql.connector` compatibility shim in `Code/mysql/`.

Tables: `users`, `students`, `teachers`, `staff`, `subjects`

---

## Tech Stack

| Layer    | Technology                   |
|----------|------------------------------|
| Language | Python 3.12                  |
| GUI      | PyQt5                        |
| Database | SQLite (mysql.connector shim)|
| Packaging| PyInstaller (Windows EXE)    |
| Deploy   | Docker + X11 forwarding      |
