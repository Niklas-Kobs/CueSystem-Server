from flask import Flask, request, jsonify, render_template
import socket
from waitress import serve
import jsonLib as jl
from time import sleep

jsonList = {
    "config": "../files/config.json", #configuration für das Projekt
    "list": "../files/list.json"
}

for key, file in jsonList.items():
    jl.libconfig(check=True, autoLoad=True, autoCreate=False, Print=True, set_reset=True, fileName=file)
    print (f"Initialisier: {key} im Pfad {file}")

app = Flask(__name__)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

@app.route('/')
def index():
    server_ip = get_local_ip()
    return render_template('index.html', ip_adresse=server_ip)

@app.route('/alive', methods=['POST'])
def alive():
    return jsonify({"[INFO]":"[Alive]"}), 200

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
    serve(app, host='0.0.0.0', port=50000, threads=6)