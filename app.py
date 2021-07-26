import flask
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return 'ddd'


# http://127.0.0.1:4000/test
@app.route("/test")
def test():
    return 'test'


# http://127.0.0.1:4000/test2
@app.route("/test2")
def test2():
    data = {"success": True, "status": "success", "message": "성공하였습니다."}
    return jsonify(data)


# http://127.0.0.1:4000/test3?name=123
@app.route("/test3")
def test3():
    name = flask.request.args.get('name')
    data = {"success": True, "status": "success", "message": "성공하였습니다.", "name": name}
    return jsonify(data)


# flask run -p 4000
if __name__ == '__main__':
    app.run(debug=True)
    # app.run('0.0.0.0', port=5000, debug=True)
