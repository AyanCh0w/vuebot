from api import getGradeInfo

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/getGradeInfo", methods=["GET"])
def hello_world():

    print(request.form['username'])
    print(request.form['password'])

    res = getGradeInfo(request.form['username'], request.form['password'])

    return jsonify(res)

app.run()