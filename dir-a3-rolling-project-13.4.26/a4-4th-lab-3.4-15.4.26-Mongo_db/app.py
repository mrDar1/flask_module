from flask import Flask, render_template

from db import init_db
from errors import errors_bp
from routes.tasks import tasks_bp


app = Flask(__name__)


init_db(app)
app.register_blueprint(tasks_bp)
# errors_bp registered last so its app_errorhandler covers all other blueprints
app.register_blueprint(errors_bp)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # debug=True only when run directly; gunicorn/production skips this block
    app.run(debug=True)
