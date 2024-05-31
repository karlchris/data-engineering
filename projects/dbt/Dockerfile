FROM fishtownanalytics/dbt:1.0.0

WORKDIR /dbt

COPY . /dbt/
COPY profiles /root/.dbt

ENV GOOGLE_APPLICATION_CREDENTIALS=/creds/application_default_credentials.json

CMD [ "executable" ]
