import jsonLib as jl

list_json = "files/list.json"

jl.libconfig(autoCreate=True)



WNR_1 = "0001"
Timeestimate_1 = "12:00"
Status_1 = "In Bearbeitung"
call_1 = None
WNR_2 = "0002"
Timeestimate_2 = "12:30"
Status_2 = "In Bearbeitung"
call_2 = None
WNR_3 = "0003"
Timeestimate_3 = "13:00"
Status_3 = "In Bearbeitung"
call_3 = None
WNR_4 = "0004"
Timeestimate_4 = "13:30"
Status_4 = "In Bearbeitung"
call_4 = None
WNR_5 = "0005"
Timeestimate_5 = "14:00"
Status_5 = "In Bearbeitung"
call_5 = None
call_6 = None
POP_H = "---"
POP_T = "---"

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
    },
    "POPUP": {
        "call_6": call_6,
        "POP_H": POP_H,
        "POP_T": POP_T
    }
    }
jl.fileName(list_json)
print (f"Filename: {list_json} | Data: {daten}")
jl.dump(daten)