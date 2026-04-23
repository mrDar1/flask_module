"""roling project - MongoDB CRUD via db.get_collection()"""
import uuid
from flask import jsonify, request, abort, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from db import get_collection


tasks_bp = Blueprint("tasks", __name__)


def _serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@tasks_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    col = get_collection("tasks")
    return jsonify({"data": [_serialize(t) for t in col.find({})]})


@tasks_bp.route("/tasks/<string:task_id>")
def get_task_byid(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": task_id})
    if task is None:
        abort(404, f"Task {task_id} not found")
    return jsonify(_serialize(task))


@tasks_bp.route("/tasks", methods=["POST"])
def post_task():
    body = request.get_json()
    if not body:
        raise BadRequest("JSON body required")
    if "title" not in body:
        raise BadRequest("title is required")

    new_task = {
        "_id": str(uuid.uuid4()),
        "title": body["title"],
        "completed": False,
    }
    col = get_collection("tasks")
    col.insert_one(new_task)
    return jsonify({"data": _serialize(new_task)}), 201


@tasks_bp.route("/tasks/<string:task_id>", methods=["PUT"])
def update_task(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": task_id})
    if task is None:
        raise NotFound(f"Task {task_id} not found")

    body = request.get_json()
    if not body:
        raise BadRequest("JSON body required")

    updates = {}
    if "title" in body:
        updates["title"] = body["title"]
    if "completed" in body:
        updates["completed"] = body["completed"]

    if updates:
        col.update_one({"_id": task_id}, {"$set": updates})
        task.update(updates)

    return jsonify(_serialize(task))


@tasks_bp.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    col = get_collection("tasks")
    task = col.find_one({"_id": task_id})
    if task is None:
        raise NotFound(f"Task {task_id} not found")

    col.delete_one({"_id": task_id})
    return jsonify({"message": f"Task '{task_id}' deleted"}), 200
