from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise NotFound(f"Task with ID {task_id} not found")
    return jsonify(task)


@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    if not request.is_json:
        raise BadRequest("Request body must be JSON")

    data = request.get_json()

    if 'title' not in data:
        raise BadRequest("Missing required field: 'title'")