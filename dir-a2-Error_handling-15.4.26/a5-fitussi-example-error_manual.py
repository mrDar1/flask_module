from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

todos = [{
    "id": 1,
    "title": "go to the gym",
    "is_completed": True
}]

# next_id = 1

# def get_todo_or_raise(todo_id):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             return todo
    # raise KeyError(f"Todo with id {todo_id} not found")


@app.errorhandler(TypeError)
def handle_type_error(e):
    return jsonify({
        "error": str(e)
    }), 400


@app.route("/todo", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todo",  methods=["POST"])
def create_todo():
    try:
        data = request.get_json()
        if data == {}:
            raise TypeError("Reauset body must be full JSON")

        title = data["title"]

        if not isinstance(title, str):
            raise TypeError("Title must be a string")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        todo = {
            "id": uuid.uuid4(),
            "title": title.strip(),
            "done": False
        }

        todos.append(todo)
        return jsonify({
            "success": True,
            "data": todo
        })
    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400

    except TypeError as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)