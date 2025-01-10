import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as F    

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

NOME_BUCKET = "anas-data-lake"
ZONE = "Trusted"
ORIGEM = "JSON"
FORMATO = "PARQUET"

caminho_fonte = args['S3_INPUT_PATH']

# Lendo o arquivo e criando o DataFrame
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type = "s3",
    connection_options = {"paths": [caminho_fonte]},
    format="json",

) 

df_transformado = dynamic_frame.toDF()

#fazendo modificações 
df_transformado = df_transformado.withColumn(
    "Provedores de Streaming",
    F.regexp_replace("Provedores de Streaming", r'\\"', '"')
)

#apenas 1 parquet
df_transformado = df_transformado.coalesce(1)

#voltando a dynamic_frame
dynamic_frame_transformado = DynamicFrame.fromDF(df_transformado, glueContext, "dynamic_frame_modificado")

#gravando no caminho em parquet
caminho_trusted = f"s3://{NOME_BUCKET}/{ZONE}/{ORIGEM}/{FORMATO}/Series/2025/01/08/"
glueContext.write_dynamic_frame.from_options(
    frame= dynamic_frame_transformado,
    connection_type = "s3",
    connection_options = {"path": caminho_trusted},
    format="parquet"
    )

job.commit()