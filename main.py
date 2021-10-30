from flask import Flask
from flask import request

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
    f = request.files['submit_code']
    f.save('uploaded_file.txt')
  #code soll danach noch gesaved werden
