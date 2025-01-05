animais = ["leão", "tigre", "elefante", "girafa", "zebra", "rinoceronte", "canguru", "urso-pardo", "golfinho", "furão",
            "lobo", "cobra", "pinguim", "tartaruga", "hipopótamo", "gato", "cachorro", "papagaio", "camaleão", "lêmure"
]

animais.sort()
[print(animal) for animal in animais]

with open ('animais.csv', 'w', encoding='utf-8') as arquivo:
   [arquivo.write(animal + "\n") for animal in animais]
    
print("Arquivo 'animais.csv' gerado com sucesso!")