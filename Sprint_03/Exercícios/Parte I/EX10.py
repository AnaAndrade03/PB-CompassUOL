Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.
['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def sem_duplicacao(lista):
    lista_sem_duplicacao = list(set(lista))
    print(lista_sem_duplicacao)

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
sem_duplicacao(lista)