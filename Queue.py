import json
from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

readError = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def handle_View():
    global readError
    try:
        with open("files/list.json", "r") as f:
            inhalt = json.load(f)
        readError = 0
        return jsonify(inhalt)
    except Exception as e:
        print (f"[ERROR] Queue File cood not be accesed")
        ERROR = {}
        ERRORdata = {
        "PNR_1":{
            "WNR-1": "---",
            "Timeestimate-1": "---",
            "Status-1": "---",
            "call-1": None
        },

        "PNR_2": {
            "WNR-2": "---",
            "Timeestimate-2": "---",
            "Status-2": "---",
            "call-2": None
        },

        "PNR_3": {
            "WNR-3": "---",
            "Timeestimate-3": "---",
            "Status-3": "---",
            "call-3": None
        },

        "PNR_4": {
            "WNR-4": "---",
            "Timeestimate-4": "---",
            "Status-4": "---",
            "call-4": None
        },

        "PNR_5":{
            "WNR-5": "---",
            "Timeestimate-5": "---",
            "Status-5": "---",
            "call-5": None
        },
        "POPUP": {
            "call_6": True,
            "POP_H": "ERROR",
            "POP_T": "Queuefile not found or corrupted"
        }}

        print ((f"Attempt: {readError}"))
        if readError >= 20:
            return jsonify (ERRORdata)
        else:
            readError = readError + 1
            return(ERROR)
            

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=55000, threads=6)