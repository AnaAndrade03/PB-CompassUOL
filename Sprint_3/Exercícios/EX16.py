def soma(string):
    mais = [int(num) for num in string.split(',')]
    return sum(mais)

string = "1,3,4,6,10,76"
resultado = soma(string)
print(resultado)