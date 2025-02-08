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
codigo_pais = "BR"

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
    
#buscando outras informações
    mais_parametros = []

    for serie in dados.get('results', []):
        tv_id = serie.get("id")
        detalhes_url = f"https://api.themoviedb.org/3/tv/{tv_id}"
        detalhes_parametros = {
            "api_key": chave_api,
            "language": tmdb.idioma
        }
        
        detalhes_response = requests.get(detalhes_url, params=detalhes_parametros)
        
        if detalhes_response.status_code == 200:
            detalhes = detalhes_response.json()
            serie["status"] = detalhes.get("status") 
            serie["last_air_date"] = detalhes.get("last_air_date")
            serie["number_of_seasons"] = detalhes.get("number_of_seasons") 
            serie["number_of_episodes"] = detalhes.get("number_of_episodes")
        else:
            serie["status"] = "Unknown"
            serie["last_air_date"] = "Unknown"
            serie["number_of_seasons"] = "Unknown"
            serie["number_of_episodes"] = "Unknown"

        providers_url = f"https://api.themoviedb.org/3/tv/{tv_id}/watch/providers"
        providers_response = requests.get(providers_url, params={"api_key": chave_api})
        
        if providers_response.status_code == 200:
            providers = providers_response.json().get('results', {}).get(codigo_pais, {}).get('flatrate', [])
            if providers:
                serie["streaming_providers"] = ", ".join(f'"{provider.get("provider_name")}"' for provider in providers)
            else:
                serie["streaming_providers"] = "Unknown"
        else:
            serie["streaming_providers"] = "Unknown"

#formatando dados de parametros para melhor analise dos dados 
    mais_parametros.append({
    "ID": serie.get("id"),
            "Título": serie.get("name"),
            "Título Original": serie.get("original_name"), 
            "Lingua Original": serie.get("original_language"),
            "Status": serie.get("status"),
            "Número de Temporadas": serie.get("number_of_seasons"),
            "Número de Episódios": serie.get("number_of_episodes"),
            "Popularidade": serie.get("popularity"),
            "Primeira data de exibição": serie.get("first_air_date"),
            "Última Data de Exibição": serie.get("last_air_date"),
            "Número de votações realizadas": serie.get("vote_count"),
            "Média de Votação (0-10)": serie.get("vote_average"),
            "Provedores de Streaming": serie.get("streaming_providers")
            
        })
    return mais_parametros

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



