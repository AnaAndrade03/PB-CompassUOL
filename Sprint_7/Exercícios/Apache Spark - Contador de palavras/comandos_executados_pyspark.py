docker pull da imagem: docker pull jupyter/all-spark-notebook

criação do container: docker run -it -p 8888:8888 --name container-exercicio -v C:\Users\andra\Projetos\PB-Compass:/home/jovyan/Projetos -notebook

execução do container com pyspark: docker exec -it container-exercicio pyspark

pegando o README.md do github (foi usado o arquivo de apresentação da raiz): import os
os.system('wget --header="Authorization: token <TOKEN GERADO> https://raw.githubusercontent.com/AnaAndrade03/PB-Compass/main/README.md')

lendo o arquivo no caminho do container: rdd = sc.textFile("/home/jovyan/diretorio/README.md")

checando para ver se o arquivo foi baixado e lido: print(rdd.take(5))

divindo o texto em palavras: palavras = rdd.flatMap(lambda linha: linha.lower().split())

filtrar palavras não vazias: palavras_filtradas = palavras.filter(lambda palavra: len(palavra) > 0)

contando a frequência de cada palavra: contagem_palavras = palavras_filtradas.map(lambda palavra: (palavra, 1)) \
                                      .reduceByKey(lambda x, y: x + y)

ordenando de maior frequência para menor: contagem_palavras_ordenada = contagem_palavras.sortBy(lambda x: x[1], ascending=False)

saída em f string: for palavra, frequencia in contagem_palavras_ordenada.collect():
...     print(f"A palavra '{palavra}' aparece {frequencia} vezes")