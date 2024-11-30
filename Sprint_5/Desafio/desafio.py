#bens tombados nas decadas de 70, 80 e 90 que se encaixam nas categorias bem imóvel e conjunto paisagístico, mostrando o número de tombamentos por municipio e a quantos anos ocorreu o tombamento.

#imports
import boto3
import pandas as pd
from datetime import datetime

session = boto3.Session(profile_name='default')

df = pd.read_csv(r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\processos-tombo.csv', sep=';', on_bad_lines='skip')

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
filtro_1.drop('denominacao_completa', axis=1, inplace=True)
filtro_1.drop('ato_legal', axis=1, inplace=True)
filtro_1.drop('livro_de_tombo', axis=1, inplace=True)
filtro_1.drop('distrito', axis=1, inplace=True)

#transformando o resultado em um novo csv
filtro_1.to_csv(r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\tratamento_dados_bens_tombados.csv', index=False, sep=';')

#mandando para o bucket
s3 = boto3.client('s3')
s3.upload_file(r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\tratamento_dados_bens_tombados.csv', 'desafiodados-sprint6', 'tratamento_dados_bens_tombados.csv')