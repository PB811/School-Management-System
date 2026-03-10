FROM python:3.12-slim

# Install Qt5 system libraries required by PyQt5
RUN apt-get update && apt-get install -y --no-install-recommends \
    libxcb-xinerama0 \
    libxcb1 \
    libx11-6 \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libfontconfig1 \
    libdbus-1-3 \
    libxkbcommon-x11-0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy project files
COPY Run.py .
COPY Code/ ./Code/

# Install Python dependencies
WORKDIR /app/Code
RUN uv sync --no-dev

# Initialize SQLite database
RUN uv run python init_sqlite.py

WORKDIR /app

# Data persistence: sms.db lives in a volume
VOLUME ["/app/Code"]

ENV PYTHONUNBUFFERED=1

CMD ["uv", "run", "--project", "Code", "python", "Run.py"]
