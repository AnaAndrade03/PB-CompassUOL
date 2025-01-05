import requests
import pandas as pd
from IPython.display import display

chave_api = "f1c499cad0e051544f5f09ea2ed6473d"
uri = f"https://api.themoviedb.org/3/discover/tv?api_key=f1c499cad0e051544f5f09ea2ed6473d&language=pt-BR&sort_by=popularity.desc&with_genres=10765,10759"

resposta = requests.get(uri)

if resposta.status_code == 200:
    data = resposta.json()
    
    series = []

    for serie in data['results']:
        df = {
            'Título': serie['name'],
            'Data de lançamento': serie['first_air_date'],
            'Visão geral': serie['overview'],
            'Votos': serie['vote_count'],
            'Média de votos': serie['vote_average'],
            'Popularidade': serie['popularity']
        }
        series.append(df)

    df = pd.DataFrame(series)
    display(df)

else:
    print(f"Erro na requisição: {resposta.status_code}")
