#bens tombados nas decadas de 70, 80 e 90 que se encaixam nas categorias bem imóvel e conjunto paisagístico, mostrando o número de tombamentos por municipio e a quantos anos ocorreu o tombamento.
#imports
import boto3
import pandas as pd
from datetime import datetime
from io import StringIO

#lendo csv do bucket
session = boto3.Session(profile_name='Ana')
s3_cliente = session.client('s3')

bucket_name = 'desafiodados-sprint6'
s3_key = 'processos-tombo.csv'

try:
    response = s3_cliente.get_object(Bucket=bucket_name, Key=s3_key)
    csv_content = response['Body'].read().decode('utf-8') 
    df = pd.read_csv(StringIO(csv_content), delimiter=';', on_bad_lines='skip')
    print("Arquivo lido do S3 com sucesso!")
except Exception as e:
    print(f"Erro ao ler o arquivo do S3: {e}")
    exit()

#definindo função data
ano_atual = datetime.now().year

# novas colunas (função converção, string, agregação)
df['ano'] = df['processo_ano'].str.split('/').str[1].astype(int)
df['decada'] = (df['ano'] // 10) * 10
df['decada'] = df['decada'].astype(str).str[2:] 
df['tombamentos_por_municipio'] = df.groupby('municipio')['municipio'].transform('count')

#operadores lógicos e função condicional
filtro_1 = df[((df['categoria'] == 'BI') | (df['categoria'] == 'CP')) & (df['ano'].between(1970, 1999))].copy()
filtro_1['está_em_bh?'] = filtro_1['municipio'].apply(lambda x: 'Sim' if x == 'Belo Horizonte' else 'Não')
filtro_1['anos_desde_o_tombamento'] = ano_atual - filtro_1['ano']

#dropando colunas 
filtro_1.drop(['denominacao_completa', 'ato_legal', 'livro_de_tombo', 'distrito'], axis=1, inplace=True)

#transformando o resultado em um novo csv e salvando localmente 
local_file_path = r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\tratamento_dados_bens_tombados.csv'
filtro_1.to_csv(local_file_path, index=False, sep=';')
print(f"Arquivo processado salvo localmente em: {local_file_path}")

#mandando o para o bucket
session = boto3.Session(profile_name='Ana')
s3 = session.client('s3')

local_file_path = r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\tratamento_dados_bens_tombados.csv'
bucket_name = 'desafiodados-sprint6'

try:
    s3.upload_file(local_file_path, bucket_name, 'tratamento_dados_bens_tombados.csv')
    print("Arquivo enviado para o S3 com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o arquivo para o S3: {e}")