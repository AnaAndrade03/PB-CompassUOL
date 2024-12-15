FROM python:3.9

RUN pip install boto3

WORKDIR /dados

COPY . .

VOLUME ["/dados"]

CMD ["python", "bucket_carregamento.py"]

