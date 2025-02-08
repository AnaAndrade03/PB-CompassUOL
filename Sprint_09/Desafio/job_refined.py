import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as F    
from pyspark.sql.functions import *

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_1', 'S3_INPUT_PATH_2'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#definindo variáveis globais
NOME_BUCKET = "anas-data-lake"
ZONE = "Refined"

#caminhos de onde os arquivos virão (variáveis de ambiente)
caminho_fonte_csv = args['S3_INPUT_PATH_1']
caminho_fonte_json = args['S3_INPUT_PATH_2']

#caminho para onde os arquivos novos deverão ser armazenados 
caminho_refined = f"s3://{NOME_BUCKET}/{ZONE}"

#lendo dados da camada trusted que foram definidas como variaveis de ambiente
json_df = spark.read.parquet(caminho_fonte_json)
csv_df = spark.read.parquet(caminho_fonte_csv)

#fazendo select nas colunas que quero 
#json
select_json = json_df.select(
    col("ID").alias("id_serie"),
    col("Título").alias("titulo"),
    col("lingua_original").alias("lingua_original"),
    col("Status").alias("status"),
    col("número_de_temporadas").alias("num_temporadas"),
    col("número_de_episódios").alias("num_episodios"),
    col("Popularidade").alias("popularidade"),
    col("primeira_data_de_exibição").alias("prim_exibicao"),
    col("última_data_de_exibição").alias("ultm_exibicao"),
    col("número_de_votações_realizadas").alias("num_votos"),
    col("média_de_votação__0-10_").alias("media_votacao"),
    col("provedores_de_streaming").alias("proved_streaming")
)

#csv
select_csv = csv_df.select(
    col("tituloOriginal").alias("titulo_original")
)

#tabelas fato, dimensão
#tabela dimensão series
dim_series = select_json.join(
    select_csv,
    select_json["titulo"] == select_csv["titulo_original"],
    "left"
).select(
    "id_serie",
    "titulo",
    "titulo_original",
    "lingua_original",
    "status",
    explode(split(col("proved_streaming"), ",")).alias("streaming")
)

#tabela fato
fato_series = select_json.select(
    "id_serie",
    "num_temporadas",
    "num_episodios",
    "prim_exibicao",
    "ultm_exibicao",
    "popularidade",
    "num_votos",
    "media_votacao"
)

#salvando as tabelas no s3 
dim_series.write.mode("overwrite").parquet(f"{caminho_refined}/dim_series")
fato_series.write.mode("overwrite").parquet(f"{caminho_refined}/fato_series")

job.commit()
