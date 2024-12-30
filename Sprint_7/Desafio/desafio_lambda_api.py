import os
import boto3
import json
import requests
from datetime import datetime
from tmdbv3api import TMDb, Discover

def lambda_handler(event, context):
    print("Iniciando a função Lambda")
    return {
        'statusCode': 200,
        'body': 'Processamento concluído'
    }

tmdb = TMDb()
chave_api = os.getenv("CHAVE_API_TMDB")
genero_id = 10765
tmdb.idioma = "pt-BR"
discover = Discover()

NOME_BUCKET = "anas-data-lake"
DATA_ATUAL = datetime.now().strftime("%Y/%m/%d")  
ORIGEM = "TMDB"
FORMATO = "JSON"

s3_client = boto3.client('s3')

def buscar_series_por_genero (chave_api, genero_id):
    url = f"https://api.themoviedb.org/3/discover/tv"
    parametros = {
        "api_key": chave_api,
        "with_genres": genero_id,
        "language": tmdb.idioma,  
        "vote_count.gte": 5000,
        "first_air_date.gte": "2010-01-01",
        "page": 1
    }
    response = requests.get(url, params=parametros)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro: {response.status_code}")
        return None

def salvar_no_bucket(dados, caminho_s3):
    try:
        s3_client.put_object(
            Bucket = NOME_BUCKET,
            Key = caminho_s3,
            Body = json.dumps(dados, ensure_ascii=False, indent=4).encode('utf-8')
        )
        print(f"Arquivo json enviado para S3: {caminho_s3}")
    except Exception as e:
        print(f"Erro ao enviar arquivo json para S3: {str(e)}")

def formatacao_json():
    dados = buscar_series_por_genero(chave_api, genero_id)
    
    if dados:

        dados_formatados = [
            {
                "ID": serie.get("id"),
                "Título": serie.get("name"),
                "Título Original": serie.get("original_name"),
                "Lingua Original": serie.get("original_language"),
                "Popularidade": serie.get("popularity"),
                "Data de lançamento": serie.get("first_air_date"),
                "Número de votações realizadas": serie.get("vote_count"),
                "Média de Votação (0-10)": serie.get("vote_average"),
            }
            for serie in dados['results']
        ]
        return dados_formatados
    return []

def processar_series_por_genero():
    dados = formatacao_json()[:10]
    
    if dados:
        dados_ordenados_votos = sorted(dados, key=lambda x: x['Número de votações realizadas'], reverse=True)
        caminho = f"{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_numero_votos.json"
        salvar_no_bucket(dados_ordenados_votos, caminho)

        dados_ordenados_media = sorted(dados, key=lambda x: x['Média de Votação (0-10)'], reverse=True)
        caminho = f"{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_media_votos.json"
        salvar_no_bucket(dados_ordenados_media, caminho)

        dados_ordenados_popularidade = sorted(dados, key=lambda x: x['Popularidade'], reverse=True)
        caminho = f"{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_popularidade.json"
        salvar_no_bucket(dados_ordenados_popularidade, caminho)

processar_series_por_genero()
