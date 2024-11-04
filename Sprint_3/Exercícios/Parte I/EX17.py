def dividindo_lista(lista):
   
    tamanho = len(lista)
   
    lista1 = lista[slice(0, 4)]
    lista2 = lista[slice(4,8)]
    lista3 = lista[slice(8,12)]
    
    return lista1, lista2, lista3

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = dividindo_lista(lista)

print(lista1, end = ' '), print(lista2, end = ' ' ), print(lista3) 
