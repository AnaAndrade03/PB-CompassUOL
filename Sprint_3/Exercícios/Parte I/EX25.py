class Aviao:
    cor = 'azul' 
    def __init__(self, modelo, velocidade_maxima,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade

avioes = list([
    Aviao('modelo BOIENG456', 'velocidade máxima de 1500 km/h', 400),
    Aviao('modelo Embraer Praetor 600', 'velocidade máxima de 863km/h', 14),
    Aviao('modelo Antonov An-2', 'velocidade máxima de 258 Km/h', 12)
])

for aviao in avioes:
    print(f"O avião de \"{aviao.modelo}\" possui uma \"{aviao.velocidade_maxima}\", capacidade para \"{aviao.capacidade}\" passageiros e é da cor \"{aviao.cor}\".")       