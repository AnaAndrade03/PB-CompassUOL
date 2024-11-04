Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
Importante: Aplique a função range().

for i in range(101):
    primo = True 
    if i <= 1:
        primo = False 
    else:
        for n in range(2, int(i**0.5) + 1):
            if i % n == 0:
                primo = False 
              
    if primo:
        print(i)