import json
from flask import Flask,request
from flask_cors import CORS
from database import get_messages,add_message

app = Flask(__name__)
CORS(app)
ids = []

@app.route("/")
def index():
    return {"messages":get_messages()}

@app.route("/post/<string:username>&<int:post_time>&<string:payload>")
def add_database(username,post_time,payload):
    ip = str(request.remote_addr)
    if ip not in ids :
        ids.append(ip)
    username = "{}(id:{})".format(username,str(ids.index(ip)))
    add_message(username,post_time,payload)
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8000)