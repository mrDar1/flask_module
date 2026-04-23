"""roling project - error handling via errors.py"""
import uuid
from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import NotFound, BadRequest
from errors import errors_bp

app = Flask(__name__)
app.register_blueprint(errors_bp)

# ########## const #################
tasks = [
    {"id": "1", "title": "Learn Flask",       "completed": False},
    {"id": "2", "title": "Build API",         "completed": False},
    {"id": "3", "title": "Test with Postman", "completed": True},
]


# * ###### helper functions ##############


def _find_task(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return jsonify(tasks)


# * ###### start logic ##############


@app.route("/")
def home():
    return jsonify({
        "message": "API is running",
    })


@app.route("/tasks/<string:task_id>")
def get_task(task_id):
    task = _find_task(task_id)
    if task is None:
        abort(404, f"Task {task_id} not found")
        # raise NotFound(f"Task {task_id} not found")
        # raise and abort do the same - raise is python, abort is flask shortcut.
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
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


@app.route("/tasks/<string:task_id>", methods=["PUT"])
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


@app.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = _find_task(task_id)
    task_temp_copy = task
    if task is None:
        raise NotFound(f"Task {task_id} not found")

    tasks.remove(task)
    # return jsonify(f"[DELETED] Task {task_temp_copy}"), 204# Correct
    return jsonify({"message": f"Task '{task_temp_copy['id']}' deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
