import os
import boto3
import json
import datetime
from tmdbv3api import TMDb, Discover

tmdb = TMDb()
tmdb_chave_api = os.getenv("CHAVE_API_TMDB")
tmdb.language = "pt-BR"
discover = Discover()

NOME_BUCKET = "anas-data-lake"
DATA_ATUAL = datetime.now().strftime("%Y/%m/%d")  
ORIGEM = "TMDB"
FORMATO = "JSON"

session = boto3.Session(profile_name='Ana')
s3_client = session.client('s3')
