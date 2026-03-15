import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/v1/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello World"})


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug)
