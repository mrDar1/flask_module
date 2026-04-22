"""roling project - here add error handling - didnt start yet"""
import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

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
        return jsonify({"error": f"Task {task_id} not found"}), 404
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def post_task():
    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body required"}), 400
    if "title" not in body:
        return jsonify({"error": "title is required"}), 400

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
        return jsonify({"error": f"Task {task_id} not found"}), 404

    body = request.get_json()
    if not body:
        return jsonify({"error": "JSON body required"}), 400

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
        return jsonify({"error": f"Task {task_id} not found"}), 404

    tasks.remove(task)
    # return jsonify(f"[DELETED] Task {task_temp_copy}"), 204# Correct
    return jsonify({"message": f"Task '{task_temp_copy['id']}' deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
