import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database # use for better IDE hint


load_dotenv()


_client = None
_db = None


def init_db(app):
    global _client, _db
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI environment variable is not set.")

    _client = MongoClient(mongo_uri)
    _db = _client["prod"]
    # app.config["DB"] = _db  # flask stuff, makes it accessible anywhere at Flask app. check if can delete it and use "get_collection" only.


def get_collection(name):
    # add security level: instead of passing db around "get" it.
    if _db is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return _db[name]
