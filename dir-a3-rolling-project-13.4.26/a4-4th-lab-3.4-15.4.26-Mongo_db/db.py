import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.database import Database # use for better IDE hint


load_dotenv()


# Module-level singletons; underscore prefix signals they are private to this module
_client = None
_db = None


# init_db called once at startup; get_collection called per-request (cheap — no new connection)
def init_db(app):
    global _client, _db
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        raise RuntimeError("MONGO_URI environment variable is not set")

    _client = MongoClient(mongo_uri)
    db_name = os.getenv("MONGO_DB_NAME", "prod")  # use db_name from .env and if not specify - defualt name is "prod"
    _db = _client[db_name]

    # check if can delete it, without break code and use "get_collection" only:
    # # flask stuff, makes it accessible anywhere at Flask app.
    # app.config["DB"] = _db


def get_collection(name):
    # add security level: instead of passing db around "get" it.
    if _db is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return _db[name]
