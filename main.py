from flask import Flask
from flask import request
import uuid

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/room/<int:number>")
def loading_room(number):
    #raum laden code hier
        return "<p>raum " + str(number) + "</p>"



@app.route('/submit_code', methods=['POST'])
def submit_code():
    dateiname = str(uuid.uuid4())
    fileExtension = ".txt"
    if request.json["language" ] == "python":
        fileExtension = ".py"
    elif request.json["language"] == "javascript":
        fileExtension = ".js"
    f = request.files['submit_code']
    f.save(dateiname + fileExtension)
    return "ok"
  #code soll danach noch gesaved werden


@app.route('/getimage/')
def semmel():
    open ('semmel')

