def my_map(lst, f):
    return list(map(f, lst))
    
def potencia(int):
    return int ** 2  
    
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(lista, potencia)
print(resultado)