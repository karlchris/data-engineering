FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app

CMD [ "executable" ]
