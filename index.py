from flask import Flask, Response, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return Response("<h1>Flask on Now 2.0</h1>", mimetype='text/html')


@app.route("/api/hello", methods=["GET"])
def hello():
    res = {"message": "hello!"}
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
