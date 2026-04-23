"""roling project - MongoDB CRUD via db.get_collection()"""
from datetime import datetime, timezone
from bson import ObjectId
from bson.errors import InvalidId
# bson import ObjectId + _to_oid(task_id) helper that converts URL strings to ObjectId, returning 404 for invalid IDs
from flask import jsonify, request, abort, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, UnprocessableEntity
from db import get_collection


tasks_bp = Blueprint("tasks", __name__)

# Whitelist prevents unknown keys from silently being stored in MongoDB
ALLOWED_UPDATE_FIELDS = {"title", "completed"}


def _to_oid(task_id):
    try:
        return ObjectId(task_id)
    except (InvalidId, TypeError):
        abort(404, f"{task_id} not found")


# Converts MongoDB's ObjectId _id to a JSON-serializable string "id"
def _serialize(task):
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "completed": task["completed"],
    }


@tasks_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    col = get_collection("tasks")
    return jsonify([_serialize(t) for t in col.find({})])


@tasks_bp.route("/tasks/<string:task_id>")
def get_task_byid(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": _to_oid(task_id)})
    if task is None:
        abort(404, f"{task_id} not found")
    return jsonify(_serialize(task))


@tasks_bp.route("/tasks", methods=["POST"])
def post_task():
    # silent=True returns None on parse error; force=True accepts any Content-Type
    body = request.get_json(silent=True, force=True)
    if not body or "title" not in body:
        raise BadRequest("request body must be json")

    title = body["title"].strip()
    if not title:
        raise UnprocessableEntity("title must contain text")

    now = datetime.now(timezone.utc)
    new_task = {
        "title": title,
        "completed": False,
        "created_at": now,
        "updated_at": now,
    }
    col = get_collection("tasks")
    col.insert_one(new_task)
    return jsonify({"success": True, "data": _serialize(new_task)}), 201


@tasks_bp.route("/tasks/<string:task_id>", methods=["PUT"])
def update_task(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": _to_oid(task_id)})
    if task is None:
        raise NotFound(f"{task_id} not found")

    body = request.get_json() or {}
    unknown = set(body) - ALLOWED_UPDATE_FIELDS
    if unknown:
        raise BadRequest(f"not allowed to pass {unknown.pop()}")

    updates = {}
    if "title" in body:
        updates["title"] = body["title"].strip()
    if "completed" in body:
        if not isinstance(body["completed"], bool):
            raise BadRequest("completed must be a boolean")
        updates["completed"] = body["completed"]

    if updates:
        updates["updated_at"] = datetime.now(timezone.utc)
        col.update_one({"_id": task["_id"]}, {"$set": updates})
        task.update(updates)  # sync local dict so _serialize reflects changes without a second DB read

    return jsonify(_serialize(task))


@tasks_bp.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": _to_oid(task_id)})
    if task is None:
        raise NotFound(f"{task_id} not found")

    col.delete_one({"_id": task["_id"]})
    return jsonify({"Message": f"removed task {task_id}"}), 200
