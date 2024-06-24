ARG MKDM_VERSION=latest

FROM squidfunk/mkdocs-material:${MKDM_VERSION}

COPY requirements.txt /root
RUN pip install -r /root/requirements.txt

COPY . .

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
