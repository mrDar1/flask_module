from datetime import datetime, timezone
from flask import Flask, jsonify


app = Flask(__name__)


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
def currentTime():
    now = datetime.now(timezone.utc).isoformat()
    return jsonify({
        "time": now
    })


if __name__ == "__main__":
    app.run(debug=True)