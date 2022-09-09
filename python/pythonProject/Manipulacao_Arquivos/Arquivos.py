import json
dicionario = {
  "CHAVES": ["Chaves", "14/04/2020", "Recep_01"],
  "QUICO": ["Quico", "08/09/2022", "Raiox_01"]
}

with open("db.json", "w") as json_file:
    json.dump(dicionario, json_file)