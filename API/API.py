import json
from flask import Flask, request, jsonify, render_template
import socket
from waitress import serve
import jsonLib as jl

jsonList = {
    "config": "../config.json",
    "data": "data.json",
    "list": "../list.json"
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

@app.route('/show', methods=['GET'])
def handle_View():
    inhalt = jl.get("PNr_2")
    return jsonify(inhalt)

@app.route('/update', methods=['POST'])
def handle_request():
    data = request.json 
    
    PNr = data.get("PNr")
    Cue_Pos = data.get("Cue_Pos")
    Call = data.get("Call")
    delete = data.get("delete")
    Time = data.get("Time")
    timecode = data.get("Timecode")
    Posttime = data.get("Posttime")
    Move = data.get("Move")

    daten = {

        PNr:{
            "Cue_Pos": Cue_Pos,
            "Call": Call,
            "delete": delete,
            "Time": Time,
            "Timecode": timecode,
            "Posttime": Posttime,
            "Move": Move
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
    #app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=50000, threads=6)