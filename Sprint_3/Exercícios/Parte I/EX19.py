import random
import statistics

random_list = random.sample(range(500), 50)
valor_minimo = min(random_list)
valor_maximo = max(random_list)
media = sum(random_list) / len(random_list)
mediana = statistics.median(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}') 
