class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def soma(self):
        return self.x + self.y
    
    def subtracao(self):
        return self.x - self.y

#VALORES
x = 4
y = 5

calculo = Calculo(x, y)

soma = calculo.soma()
subtracao = calculo.subtracao()

print(f"Somando: {x} + {y} = {soma}")
print(f"Subtraindo: {x} - {y} = {subtracao}")