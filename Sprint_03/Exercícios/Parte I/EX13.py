Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
Dica: leia a documentação da função open(...)

arquivo = 'arquivo_texto.txt'

with open(arquivo, mode = 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo, end='')
