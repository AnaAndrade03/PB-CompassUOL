from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Exercicio Intro") \
    .getOrCreate()

#lendo o arquivo e mostrando as cinco primeira linhas (ETAPA 1)
df_nomes = spark.read.csv(r"C:\Users\andra\Projetos\PB-Compass\Sprint_8\Exercícios\Apache Spark\nomes-aleatorios.txt")
df_nomes.show(5)

#nomeando a coluna não nomeada anteriormente (nomes) (ETAPA 2)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes") 
df_nomes.printSchema()
df_nomes.show(10)

#criando coluna Escolaridade (ETAPA 3)
escolaridades = ["Fundamental", "Medio", "Superior"]

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    expr(f"split('{','.join(escolaridades)}', ',')[cast(rand() * 3 as int)]")
)

df_nomes.show(10)   

#criando coluna Pais (ETAPA 4)
paises = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", 
    "Equador", "Guiana", "Paraguai", "Peru", "Suriname", 
    "Uruguai", "Venezuela", "Guiana Francesa"
]

df_nomes = df_nomes.withColumn(
    "Pais",
    expr(f"split('{','.join(paises)}', ',')[cast(rand() * 13 as int)]")
)

df_nomes.show(10)

#criando coluna AnoNascimento (ETAPA 5)
df_nomes = df_nomes.withColumn(
    "AnoNascimento", 
    (floor(rand() * (2010 - 1945 + 1)) + 1945)
)

df_nomes.show(10)

#selecionando pessoas que nasceram nese seculo (ETAPA 6) 
df_selecao = df_nomes.select("*").filter(df_nomes.AnoNascimento >=2001)
df_selecao.show(10)

#selecionando pessoas que nasceram nesse seculo usando spark SQL (ETAPA 7)
df_nomes.createOrReplaceTempView("pessoas")

df_selecao_sql = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2001")

df_selecao_sql.show()

#contando o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) (ETAPA 8)
contagem_millennials = df_nomes.filter((df_nomes.AnoNascimento >=1980) & (df_nomes.AnoNascimento <=1994)).count()

print(f'Número de Millennials: {contagem_millennials}')

#contando o número de pessoas que são da geração Millennials (nascidos entre 1980 e 1994) usando spark SQL  (ETAPA 9)
df_nomes.createOrReplaceTempView("pessoas")
df_numero_millennials_sql = spark.sql("""
    SELECT COUNT(*) AS df_numero_millennials_sql
    FROM pessoas
    WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

df_numero_millennials_sql.show()

#quantidade de pessoas de cada país para cada uma das gerações (ETAPA 10)
#Baby Boomers nascidos entre 1944 e 1964;
#Geração X — nascidos entre 1965 e 1979;4
#Millennials (Geração Y) — nascidos entre 1980 e 1994;
#Geração Z— nascidos entre 1995 e 2015.
df_nomes.createOrReplaceTempView("pessoas")

df_contagem_geracoes = spark.sql("""
    SELECT Pais,
            CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'                    
            ELSE 'Desconhecido'       
        END AS Geracao,
           COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao              
""")

df_contagem_geracoes.show()