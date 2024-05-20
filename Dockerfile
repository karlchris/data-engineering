ARG MKDM_VERSION=latest

FROM squidfunk/mkdocs-material:${MKDM_VERSION}

COPY . .

# Start development server by default
ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
