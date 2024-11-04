arquivo = 'arquivo_texto.txt'

with open(arquivo, mode = 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo, end='')
