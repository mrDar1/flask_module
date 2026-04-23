from flask import Flask, render_template

from db import init_db, get_collection
from errors import errors_bp
from routes.tasks import tasks_bp, _serialize


app = Flask(__name__)
init_db(app)
app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)


@app.route("/", methods=["GET"])
def index():
    col = get_collection("tasks")
    initial_tasks = [_serialize(t) for t in col.find({})]
    # fetches all documents from a MongoDB collection and serializes them.
    # converts it to a string so the document can be returned as JSON from a Flask route

    return render_template("index.html", initial_tasks=initial_tasks)


if __name__ == "__main__":
    app.run(debug=True)
