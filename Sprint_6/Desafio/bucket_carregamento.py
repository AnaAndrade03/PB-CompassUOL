#imports

import boto3 
import os
from datetime import datetime
from botocore.exceptions import ClientError

#definições
NOME_BUCKET = "anas-data-lake"  
RAW_ZONE = "Raw"
ORIGEM = "Local"
FORMATO = "CSV"
DATA_ATUAL = datetime.now().strftime("%Y/%m/%d")  

session = boto3.Session(profile_name='Ana')
s3_client = session.client('s3')

#criando bucket 
try:
    response = s3_client.create_bucket(Bucket = NOME_BUCKET)
    print(f"Bucket {NOME_BUCKET} criado com sucesso.")
except ClientError as e:
    print(f"Erro ao criar o bucket {NOME_BUCKET}: {e}")

#lendo os arquivos e mandando para o bucket que acabou de ser criado com o path especifico
arquivos_para_enviar = [
    '/dados/movies.csv', 
    '/dados/series.csv'   
]

s3_keys = f"{RAW_ZONE}/{ORIGEM}/{FORMATO}/Movies/{DATA_ATUAL}/movies.csv", f"{RAW_ZONE}/{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/series.csv"

for local_file_path, s3_key in zip(arquivos_para_enviar, s3_keys):
    try:
        s3_client.upload_file(local_file_path, NOME_BUCKET, s3_key)
        print(f"Upload de {local_file_path} para {NOME_BUCKET}/{s3_key} concluído!")
    except Exception as e:
        print(f"Erro ao enviar {local_file_path} para o bucket: {e}")
 

 