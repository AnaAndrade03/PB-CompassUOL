FROM python:3.9

RUN pip install boto3

WORKDIR /dados

COPY ./Desafio/movies.csv /dados/movies.csv
COPY ./Desafio/series.csv /dados/series.csv

COPY ./Desafio/bucket_carregamento.py /dados/bucket_carregamento.py

VOLUME ["/dados"]

CMD ["python", "bucket_carregamento.py"]

