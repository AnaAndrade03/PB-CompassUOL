import hashlib
while True:
    descubra = input("Está pronto para uma aventura no mundo das hashes? Digite algo e veja o que acontece... (ou 'sair' para escapar do desafio!)")
    
    if descubra.lower() == "sair":
        print("Você conseguiu escapar do desafio... Mas será que você encontrou todas as respostas? Até a próxima, explorador!")
        break
    
    hash_hex = hashlib.sha1(descubra.encode()).hexdigest()
    
    if len(descubra) < 5:
        print(f'Isso foi mais fácil que escalar uma montanha de marshmallows! Sua hash de: {descubra} é: {hash_hex}')
    else:
        print(f'Eu sabia que algo misterioso estava por vir... Sua hash de: {descubra} é: {hash_hex}')