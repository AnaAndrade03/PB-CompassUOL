E03
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map
------------------------------------------------------------

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    valores = map(lambda item: item[0] if item[1] =='C' else -item[0], lancamentos)
    saldo = reduce(lambda saldo_atual, valor: saldo_atual + valor, valores, 0)
    return saldo
