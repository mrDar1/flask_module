from flask import Flask, request
from markupsafe import escape
# escape convert user text to safe string - disable any script

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app.run(debug=True)
