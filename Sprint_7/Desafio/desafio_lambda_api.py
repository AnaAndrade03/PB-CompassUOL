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
RAW_ZONE = "Raw"
ORIGEM = "TMDB"
FORMATO = "JSON"

s3_client = boto3.client('s3')

#busca as series com o genero pedido e as formata para melhor visualização no arquivo json final.
def buscar_e_formatar_series(chave_api, genero_id):
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
        print("Busca bem-sucedida! Dados do TMDB recebidos com sucesso.")
    else:
        print(f"Erro na busca. Código de status: {response.status_code}")
        return []
    
    dados = response.json()
    if not dados:
        return []
    
#formatando dados de parametros para melhor analise dos dados 
    return [
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
        for serie in dados.get('results', [])
    ]

# Função que salva arquivo no bucket
def salvar_no_bucket(dados, caminho_s3):
    try:
        s3_client.put_object(
            Bucket = NOME_BUCKET,
            Key = caminho_s3,
            Body = json.dumps(dados, ensure_ascii=False, indent=4).encode('utf-8')
        )
        print(f"Arquivo json enviado com sucesso para bucket anas-data-lake!: {caminho_s3}")
    except Exception as e:
        print(f"Erro ao enviar arquivo json para S3: {str(e)}")

# Função que processa os dados que que vão compor 3 arquivos json, cada um com uma ordenação diferente.
def processar_series_por_genero():
    dados = buscar_e_formatar_series()[:10]
    
    if dados:
        dados_ordenados_votos = sorted(dados, key=lambda x: x['Número de votações realizadas'], reverse=True)
        caminho = f"{RAW_ZONE}/{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_numero_votos.json"
        salvar_no_bucket(dados_ordenados_votos, caminho)

        dados_ordenados_media = sorted(dados, key=lambda x: x['Média de Votação (0-10)'], reverse=True)
        caminho = f"{RAW_ZONE}/{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_media_votos.json"
        salvar_no_bucket(dados_ordenados_media, caminho)

        dados_ordenados_popularidade = sorted(dados, key=lambda x: x['Popularidade'], reverse=True)
        caminho = f"{RAW_ZONE}/{ORIGEM}/{FORMATO}/Series/{DATA_ATUAL}/ordenado_popularidade.json"
        salvar_no_bucket(dados_ordenados_popularidade, caminho)

processar_series_por_genero()
