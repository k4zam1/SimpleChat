import json
from flask import Flask
from flask_cors import CORS
from database import get_messages,add_message

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    ret = {"messages":[]}
    messages = list(get_messages())
    for i in range(len(messages)):
        messages[i]["_id"] = str(messages[i]["_id"])
        ret["messages"].append(messages[i])
    return ret

@app.route("/post/<username>&<int:post_time>&<string:payload>")
def add_database(username,post_time,payload):
    add_message(username,post_time,payload)
    return ""
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=8000)