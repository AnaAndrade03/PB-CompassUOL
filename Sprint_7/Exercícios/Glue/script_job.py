import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, upper, count, desc, sum
from pyspark.sql.window import Window

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

caminho_fonte = args['S3_INPUT_PATH']
caminho_destino = args['S3_TARGET_PATH']

# Lendo o arquivo e criando o DataFrame
df = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_fonte]},
    format="csv",
    format_options={"withHeader": True, "separator": ","}
)

# Convertendo para DataFrame Spark
df_spark = df.toDF()
df_spark.printSchema()

# Convertendo o nome para maiúsculas
df_spark = df_spark.withColumn("nome", upper(col("nome")))

# Contagem de linhas
print(f"Número de linhas: {df_spark.count()}")

#contagem de anos agrupados
contagem_nomes = df_spark.groupBy("ano", "sexo").count().orderBy("ano", ascending = False)
contagem_nomes.show()

#nome feminino mais registrado 
nomes_fem = df_spark.filter(col("sexo") == "F").groupBy("nome", "ano").agg(
    sum("total").alias("registros_fem"
))
nome_mais_popular_fem = nomes_fem.orderBy(col("registros_fem").desc()).first()
print(f'O nome feminino com mais registro é: {nome_mais_popular_fem["nome"]}, no ano: {nome_mais_popular_fem["ano"]}, com {nome_mais_popular_fem["registros_fem"]} registros')

#nome masculino mais registrado 
nomes_masc = df_spark.filter(col("sexo") == "M").groupBy("nome", "ano").agg(
    sum("total").alias("registros_masc"
))
nome_mais_popular_masc = nomes_masc.orderBy(col("registros_masc").desc()).first()

print(f'O nome masculino com mais registro é: {nome_mais_popular_masc["nome"]}, no ano: {nome_mais_popular_masc["ano"]}, com {nome_mais_popular_masc["registros_masc"]} registros')

#registros por ano
registros_ano = df_spark.groupBy("ano").agg(count("*").alias("total de registros por ano"))
registros_ordenados = registros_ano.orderBy("ano").limit(10)
registros_ordenados.show()

#escrevendo
df_spark.write.partitionBy("sexo", "ano").mode("overwrite").json(caminho_destino)
job.commit()