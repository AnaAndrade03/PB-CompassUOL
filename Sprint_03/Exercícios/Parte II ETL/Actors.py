#Exercício1
with open('actors.csv', 'r') as arquivo:
    resultado = [linha.rsplit(',', 5) for linha in arquivo]

nome = ""
qtd_maior = 0

for coluna in resultado[1:]:
    num_filmes = int(coluna[2])  
    if num_filmes > qtd_maior:
        nome = coluna[0]  
        qtd_maior = num_filmes 
print(nome, qtd_maior)

with open ('etapa-1.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade:')
    text.write('\nAtor com mais filmes: {}, quantidade filmes: {}.'.format(nome, qtd_maior))
  
#Exercício2
with open('actors.csv', 'r') as arquivo:
    resultado = [linha.strip().split(',') for linha in arquivo]

with open('etapa-2.txt', 'a', encoding='utf-8') as text:
    for coluna in resultado[1:]:  
        fat_total = coluna[3].replace('"', '')  
        text.write('Ator/atriz {}, possui média de faturamento bruto de {}.\n'.format(coluna[0], fat_total))

#Exercício 3 
with open('actors.csv', 'r') as arquivo:
    resultado = [linha.rsplit(',', 5) for linha in arquivo]

atorfatura = ""
maiorfaturamento = 0

for coluna in resultado[1:]: 
    faturamento = float(coluna[3])  
    if faturamento > maiorfaturamento:  
        maiorfaturamento = faturamento  
        atorfatura = coluna[0] 
print(atorfatura, maiorfaturamento)

with open ('etapa-3.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior média de faturamento por filmes:')
    text.write('\nAtor/atriz com a maior média de faturamento por filme é {} com média {}.'.format(atorfatura, maiorfaturamento))

#Exercício4
frequencia = {}  
with open('actors.csv', 'r') as file:
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
with open('actors.csv', 'r') as arquivo:
    resultado = [linha.rsplit(',', 5) for linha in arquivo]

for coluna in resultado [1::]:
    with open ('etapa-5.txt', 'at', encoding='utf-8') as text:
        text.write('Ator: {} | Faturamento Bruto Total: {}\n'.format(coluna[0],coluna[1]).replace('"',''))
