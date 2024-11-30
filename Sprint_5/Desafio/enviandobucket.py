import boto3 

session = boto3.Session(profile_name='default')

s3 = boto3.client('s3')
s3.upload_file(r'C:\Users\andra\OneDrive\Área de Trabalho\desafio\processos-tombo.csv', 'desafiodados-sprint6', 'processos-tombo.csv')