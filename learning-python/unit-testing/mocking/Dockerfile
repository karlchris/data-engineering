FROM python:3.9-slim

WORKDIR /test

COPY . /test/

RUN pip install pytest==8.2.0 pytest-mock==3.14.0

CMD pytest
