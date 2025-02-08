Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
Dica: leia a documentação do pacote json

import json 

with open("person.json") as pessoa_json:
    dados = json.load(pessoa_json)

print (dados)
