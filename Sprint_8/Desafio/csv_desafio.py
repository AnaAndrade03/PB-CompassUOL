import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

NOME_BUCKET = "anas-data-lake"
ZONE = "Trusted"
ORIGEM = "CSV"
FORMATO = "PARQUET"

caminho_fonte = args['S3_INPUT_PATH']

#lendo o arquivo e criando o DataFrame
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [caminho_fonte]},
    format="csv",
    format_options={"withHeader": True, "separator": "|"}
)

#transformando em data frame para modificar 
df_transformado = dynamic_frame.toDF()

#removendo colunas sobre atores porque não vou usar esse tipo de informação
remocao_colunas = [
    "generoArtista", "personagem", "nomeArtista", "anoNascimento",
    "anoFalecimento", "profissao", "titulosMaisConhecidos", "anoTermino"
]

df_transformado = df_transformado.drop(*remocao_colunas)

#convertendo datatypes para consultar no lambda depois 
df_transformado = df_transformado.withColumn("notaMedia", col("notaMedia").cast(FloatType()))
df_transformado = df_transformado.withColumn("anoLancamento", to_date(col("anoLancamento").cast("string"), "yyyy"))
df_transformado = df_transformado.withColumn("numeroDeVotos", col("numeroDeVotos").cast(IntegerType()))
df_transformado = df_transformado.withColumn("tempoEmMinutos", col("tempoEmMinutos").cast(IntegerType()))

#filtrando séries a partir de 2010
df_transformado = df_transformado.filter(col("anoLancamento") >= 2010)

#filtrando series que tenha algum desses generos na descrição (algumas são misturadas)
df_transformado = df_transformado.filter(
    lower(col("genero")).contains("fantasy") | lower(col("genero")).contains("sci-fi")
)

#dropando repetições
df_transformado= df_transformado.dropDuplicates()

#voltando a dynamic_frame
dynamic_frame_transformado = DynamicFrame.fromDF(df_transformado, glueContext, "dynamic_frame_transformado")

#gravando no caminho em parquet
caminho_trusted = f"s3://{NOME_BUCKET}/{ZONE}/{ORIGEM}/{FORMATO}/Series/"
glueContext.write_dynamic_frame.from_options(
    frame= dynamic_frame_transformado,
    connection_type = "s3",
    connection_options = {"path": caminho_trusted},
    format="parquet"
)

job.commit()