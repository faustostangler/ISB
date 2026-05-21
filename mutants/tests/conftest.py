import os

# Set dummy environment variables for pytest collection to prevent fail-fast validation
# errors when importing modules that instantiate settings on load.
# Specific tests will monkeypatch these variables to test validation constraints.
os.environ.setdefault("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/test_db")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
