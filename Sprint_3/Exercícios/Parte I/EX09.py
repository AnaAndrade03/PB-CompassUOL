primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
for index, (primeirosNomes, sobreNomes, idades) in enumerate(zip(primeirosNomes,sobreNomes,idades)):
    print (f'{index} - {primeirosNomes} {sobreNomes} está com {idades} anos')