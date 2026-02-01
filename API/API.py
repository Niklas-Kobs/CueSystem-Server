import json
from flask import Flask, request, jsonify, render_template
import socket
from waitress import serve
import jsonLib as jl

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

@app.route('/update', methods=['POST'])
def handle_request():
    data = request.json 
    
    PNR_1 = data.get("PNR_1")
    WNR_1 = data.get("WNR-1")
    Timeestimate_1 = data.get("Timeestimate-1")
    PNR_1 = data.get("PNR_1")
    PNR_1 = data.get("PNR_1")

    daten = {
        "PNR_1": {
        "WNR-1": "#0001",
        "Timeestimate-1": "12:00",
        "Status-1": "Waiting",
        "call-1": True
        }
    }

    if jl.get(PNr) == None and jl.addlist (daten):
        print(f"Empfangen: {daten} für Patient {PNr}")
    elif jl.get(PNr) != None:
        jl.dump (daten)
        print(f"Aktualisiert: {daten} für Patient {PNr}")
    else:
        print(f"Fehler beim Hinzufügen der Daten für Patient {PNr}")


    return jsonify({"status": "Erfolgreich empfangen"}), 200

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=50000, threads=6)