"""roling project"""
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException, NotFound
from routes import tasks_bp
from models import get_all_tasks

app = Flask(__name__)


task_id_counter = 4

app.register_blueprint(tasks_bp)




# ###### helper functions ##############


def _find_task(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)


# ###### start logic ##############


@app.route("/")
def home():
    return jsonify({
        "message": "API is runnning",
    })


@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    task = _find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task {task_id} not found"}), 404
    return jsonify(task)


@app.route("/tasks", methods=["POST"])
def post_task():
    global task_id_counter
    body = request.get_json()

    new_task = {
        "id": task_id_counter,
        "title": body["title"],
        "completed": False,
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = _find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task {task_id} not found"}), 404

    body = request.get_json()

    if "title" in body:
        task["title"] = body["title"]
    if "completed" in body:
        task["completed"] = body["completed"]

    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = _find_task(task_id)
    if task is None:
        return jsonify({"error": f"Task {task_id} not found"}), 404

    tasks.remove(task)
    return jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)
