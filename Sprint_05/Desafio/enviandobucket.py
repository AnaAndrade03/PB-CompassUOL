import boto3 

session = boto3.Session(profile_name='Ana')
s3 = session.client('s3')

local_file_path = r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\processos-tombo.csv'
bucket_name = 'desafiodados-sprint6'
s3_key = 'processos-tombo.csv'

try:
    s3.upload_file(local_file_path, bucket_name, s3_key)
    print(f"Arquivo '{local_file_path}' enviado com sucesso para o bucket '{bucket_name}' com a chave '{s3_key}'.")
except Exception as e:
    print(f"Erro ao enviar o arquivo para o S3: {e}")