#Exercício1
with open('actors.csv', 'r') as arquivo:
    resultado = []
    for linha in arquivo:
        palavras = linha.rsplit(',', 5)
        resultado.append(palavras[:])

num_filmes = []
for coluna in resultado[1::]:
    num_filmes.append(coluna[2])
    qtd_maior = max(num_filmes)
    if coluna[2] == qtd_maior:
        nome = coluna[0]
print(nome, qtd_maior)

with open ('etapa-1.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade:')
    text.write('\nAtor com mais filmes: {}, quantidade filmes: {}.'.format(nome, qtd_maior))
    text.close() 


#Exercício2
with open('actors.csv', 'r') as arquivo:
    resultado = [linha.rsplit(',', 5) for linha in arquivo]

with open('etapa-2.txt', 'a', encoding='utf-8') as text:
    for coluna in resultado[1:]:
        fat_total = coluna[3].replace('"', '')
        text.write('Ator/atriz {}, possui média de faturamento bruto de {}.\n'.format(coluna[0], fat_total))

#Exercício 3 
with open('actors.csv', 'r') as file:
   with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

maiorfaturamento = []
atorfatura = 0
for coluna in resultado[1::]:
    maiorfaturamento.append(float(coluna[3]))
    maximo = max(maiorfaturamento)
    if float(coluna[3]) >= maximo:
        atorfatura = coluna[0]

with open ('etapa-3.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior média de faturamento por filmes:')
    text.write('\nAtor/atriz com a maior média de faturamento por filme é {} com média {}.'.format(atorfatura, maximo))

#Exercício4
with open('actors.csv', 'r') as file:
    frequencia = {} 
    for linha in file:
        palavras = linha.strip().split(',')  
        filme = palavras[4].strip()  
        
        if filme in frequencia:
            frequencia[filme] += 1
        else:
            frequencia[filme] = 1

nomefrequente = max(frequencia, key=frequencia.get)
nfrequencia = frequencia[nomefrequente]

with open('etapa-4.txt', 'w', encoding='utf-8') as text:
    text.write('O nome dos filmes mais frequentes e sua respectiva frequência:\n')
    text.write('O nome do filme mais frequente é "{}" e sua frequência é {}.'.format(nomefrequente, nfrequencia))

#Exercicio 5 
with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

for coluna in resultado [1::]:
    with open ('etapa-5.txt', 'at', encoding='utf-8') as text:
        text.write('Ator: {} | Faturamento Bruto Total: {}\n'.format(coluna[0],coluna[1]).replace('"',''))