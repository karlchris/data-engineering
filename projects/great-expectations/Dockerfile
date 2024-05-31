FROM python:3.9

WORKDIR /app

RUN pip install great-expectations==0.18.15 && \
    pip install sqlalchemy-bigquery==1.11.0

COPY . /app

ENV GOOGLE_APPLICATION_CREDENTIALS=/creds/application_default_credentials.json

CMD [ "executable" ]
