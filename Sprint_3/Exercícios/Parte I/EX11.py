import json 

with open("person.json") as pessoa_json:
    dados = json.load(pessoa_json)

print (dados)
