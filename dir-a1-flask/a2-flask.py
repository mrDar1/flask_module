from flask import Flask, jsonify
from datetime import datetime, timezone


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def status():
    return jsonify({
        "status": "ok",
        "versions": "1.0.0"
    })


@app.route("/time")
def current_time():
    now_time = datetime.now(timezone.utc).isoformat()
    return jsonify({
        "time": now_time
    })


if __name__ == "__main__":
    app.run(debug=True)
