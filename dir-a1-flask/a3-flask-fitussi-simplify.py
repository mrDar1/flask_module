from datetime import datetime, timezone
from flask import Flask, jsonify, request


app = Flask(__name__)


USERS = [
    {"name": "Alice",   "ID": 1, "hobbies": ["reading", "hiking"],       "birth_place": "New York"},
    {"name": "Bob",     "ID": 2, "hobbies": ["gaming", "cooking"],        "birth_place": "London"},
    {"name": "Carol",   "ID": 3, "hobbies": ["painting", "yoga"],         "birth_place": "Tel Aviv"},
    {"name": "David",   "ID": 4, "hobbies": ["cycling", "photography"],   "birth_place": "Paris"},
    {"name": "Eva",     "ID": 5, "hobbies": ["dancing", "traveling"],     "birth_place": "Berlin"},
]


@app.route("/")
def home():
    return jsonify({
        "message": "API is runnning"
    })


@app.route("/status")
def status():
    return jsonify({
        "status": "Ok",
        "version": "1.0.0"
    })


@app.route("/time")
def current_time():
    now = datetime.now(timezone.utc).isoformat()
    return jsonify({
        "time": now
    })


@app.route("/info")
def info():
    return jsonify({
        "app": "Flask Practice",
        "author": "student",
        "day": 2
    })


@app.route("/echo", methods=["POST"])
def echo():
    body = request.json  # fitussi simpler way

    if not bool(body):
        return jsonify({
            "succuess": "False",
            "message:": "json body required"
        }), 400  # flask shourtcut: will return status code

    return jsonify({
        "succuess": "True",
        "echo": body
    })


# to use at Postman:
# http://127.0.0.1:5000/search?name=alice
@app.route("/search")
def search():
    name = request.args.get("name")

    if not name:
        return jsonify({
            "success": "False",
            "eror:": "name is required"
        }), 400

    results = []
    for user in USERS:
        if user["name"].lower() == name.lower():
            results.append(user)

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)