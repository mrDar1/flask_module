"""Pytest fixtures and test configuration for the tasks API."""
import os
from pathlib import Path
import sys

import mongomock
import pytest

# Add project root to sys.path so app modules are importable without installing the package
APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

os.environ.setdefault("MONGO_URI", "mongodb://localhost:27017/")
os.environ.setdefault("MONGO_DB_NAME", "testdb")

# Patch MongoClient before importing app so init_db uses mongomock
_patcher = mongomock.patch()
_patcher.start()

from app import app  # noqa: E402
import db            # noqa: E402

SEED_TASKS = [
    {"title": "Learn Flask",       "completed": False},
    {"title": "Build API",         "completed": False},
    {"title": "Test with Postman", "completed": True},
]


@pytest.fixture
def _mongo_tasks():
    col = db.get_collection("tasks")
    col.drop()
    col.insert_many([dict(t) for t in SEED_TASKS])
    yield col
    col.drop()


@pytest.fixture
def client(_mongo_tasks):  # _mongo_tasks injected for its side-effect (seed + teardown), value unused
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client
