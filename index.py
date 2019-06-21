import random

from flask import Flask, Response, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return Response("<h1>Flask on Now 2.0</h1>", mimetype='text/html')


@app.route("/api/hello", methods=["GET"])
def hello():
    res = {"message": "hello!"}
    return jsonify(res), 200


@app.route("/api/echo", methods=["GET"])
def echo():
    call = request.args.get("call", "")
    rand_int = random.randint(0, 10)
    call_list = [call for i in range(0, rand_int)]
    msg = "...".join(call_list)
    res = {"message": msg}
    return jsonify(res), 200


if __name__ == '__main__':
    app.run(debug=True)
