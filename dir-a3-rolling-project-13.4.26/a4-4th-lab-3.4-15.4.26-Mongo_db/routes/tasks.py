"""roling project - error handling via errors.py"""
from flask import jsonify, request, abort, Blueprint
from werkzeug.exceptions import NotFound, BadRequest
from errors import errors_bp


tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(tasks)


@tasks_bp.route("/")
def home():
    return jsonify({
        "message": "API is running",
    })


@tasks_bp.route("/tasks/<string:task_id>")
def get_task(task_id):
    task = _find_task(task_id)
    if task is None:
        abort(404, f"Task {task_id} not found")
        # raise NotFound(f"Task {task_id} not found")
        # raise and abort do the same - raise is python, abort is flask shortcut.
    return jsonify(task)


@tasks_bp.route("/tasks", methods=["POST"])
def post_task():
    body = request.get_json()
    if not body:
        raise BadRequest("JSON body required")
    if "title" not in body:
        raise BadRequest("title is required")

    new_task = {
        "id": str(uuid.uuid4()),
        "title": body["title"],
        "completed": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


@tasks_bp.route("/tasks/<string:task_id>", methods=["PUT"])
def update_task(task_id):
    task = _find_task(task_id)
    if task is None:
        raise NotFound(f"Task {task_id} not found")

    body = request.get_json()
    if not body:
        raise BadRequest("JSON body required")

    if "title" in body:
        task["title"] = body["title"]
    if "completed" in body:
        task["completed"] = body["completed"]

    return jsonify(task)


@tasks_bp.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = _find_task(task_id)
    task_temp_copy = task
    if task is None:
        raise NotFound(f"Task {task_id} not found")

    tasks.remove(task)
    # return jsonify(f"[DELETED] Task {task_temp_copy}"), 204# Correct
    return jsonify({"message": f"Task '{task_temp_copy['id']}' deleted"}), 200
