E01
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.
------------------------------------------------------------------------------------------
    
with open ('number.txt', 'r') as arquivo_num:
    numeros = list(map(int, arquivo_num.readlines()))
numeros_pares = filter(lambda int: int % 2 == 0, numeros)
maiores_numeros = sorted(numeros_pares, reverse= True)
cinco_maiores = maiores_numeros[:5]
soma = sum(cinco_maiores)

print(cinco_maiores)
print(soma)
