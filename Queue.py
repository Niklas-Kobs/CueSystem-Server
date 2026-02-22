import json
from flask import Flask, request, jsonify, render_template
from waitress import serve
from time import sleep
import jsonLib as jl

app = Flask(__name__)

jsonList = {
    "config": "../files/config.json", #configuration für das Projekt
    "list": "../files/list.json"
}

for key, file in jsonList.items():
    jl.libconfig(check=True, autoLoad=True, autoCreate=False, Print=True, set_reset=True, filename=file)
    print (f"Initialisier: {key} im Pfad {file}")

readError = 0
#Web Queue Interface
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


#API Endpoint to execute Orders

@app.route('/execute', methods=['POST'])
def execute():
    exemsg = request.json
    exe = exemsg.get("exe")

    if exe == "1":
        print ("Execute Order 1")

    return jsonify({"[INFO]":exe}), 200

@app.route('/update', methods=['POST'])
def handle_request():
    data = request.json 
    
    PNR_1 = data.get("PNR_1")
    WNR_1 = data.get("WNR_1")
    Timeestimate_1 = data.get("Timeestimate_1")
    Status_1 = data.get("Status_1")
    call_1 = data.get("call_1")

    PNR_2 = data.get("PNR_2")
    WNR_2 = data.get("WNR_2")
    Timeestimate_2 = data.get("Timeestimate_2")
    Status_2 = data.get("Status_2")
    call_2 = data.get("call_2")

    PNR_3 = data.get("PNR_3")
    WNR_3 = data.get("WNR_3")
    Timeestimate_3 = data.get("Timeestimate_3")
    Status_3 = data.get("Status_3")
    call_3 = data.get("call_3")

    PNR_4 = data.get("PNR_4")
    WNR_4 = data.get("WNR_4")
    Timeestimate_4 = data.get("Timeestimate_4")
    Status_4 = data.get("Status_4")
    call_4 = data.get("call_4")

    PNR_5 = data.get("PNR_5")
    WNR_5 = data.get("WNR_5")
    Timeestimate_5 = data.get("Timeestimate_5")
    Status_5 = data.get("Status_5")
    call_5 = data.get("call_5")

    daten = {
     "PNR_1": {
        "WNR_1": WNR_1,
        "Timeestimate_1": Timeestimate_1,
        "Status_1": Status_1,
        "call_1": call_1
    },
    "PNR_2": {
        "WNR_2": WNR_2,
        "Timeestimate_2": Timeestimate_2,
        "Status_2": Status_2,
        "call_2": call_2
    },
    "PNR_3": {
        "WNR_3": WNR_3,
        "Timeestimate_3": Timeestimate_3,
        "Status_3": Status_3,
        "call_3": call_3
    },
    "PNR_4": {
        "WNR_4": WNR_4,
        "Timeestimate_4": Timeestimate_4,
        "Status_4": Status_4,
        "call_4": call_4
    },
    "PNR_5": {
        "WNR_5": WNR_5,
        "Timeestimate_5": Timeestimate_5,
        "Status_5": Status_5,
        "call_5": call_5
    }
    }

    if jl.addlist (daten):
        pass
        #print(f"Empfangen: {daten}")
    else:
        print(f"Fehler beim Hinzufügen von: {daten}")


    return jsonify({"status": "Erfolgreich empfangen"}), 200
            

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=55000, threads=6)