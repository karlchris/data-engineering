MKDM_VERSION=9.5.24
PWD=`pwd`
PORT=8000
IMG=de-kchrs
USER := `whoami | tr . _`
GCP_AUTH := ${HOME}/.config/gcloud


# Build docker image for local development
build-docker:
	@docker build . -f Dockerfile \
		-t ${IMG}:dev \
		--build-arg MKDM_VERSION=${MKDM_VERSION}

# Run dev server in docker
dev:
	@echo "Starting dev server in a docker container"
	@docker run \
		--rm -it \
		-p 127.0.0.1:${PORT}:8000 \
		-v ${PWD}:/docs \
		${IMG}:dev

build-dbt:
	@echo "Building dbt image"
	@docker build -f projects/dbt/Dockerfile projects/dbt \
	-t dbt

run-dbt:
	@echo "Running dbt in container"
	@docker run \
		-e DESTINATION=${USER} \
		-e DBT_ENV=dev \
		--rm \
		-v ${GCP_AUTH}:/creds -it \
		--entrypoint /bin/bash \
		-p 8082:8080 \
		dbt
