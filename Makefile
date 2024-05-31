MKDM_VERSION=9.5.24
PWD=`pwd`
PORT=8000
IMG=de-kchrs
USER := `whoami | tr . _`
GCP_AUTH := ${HOME}/.config/gcloud


clean:
	@docker stop $(docker ps -q) && \
	docker system prune -f

# Build docker image for local development
build-page:
	@echo "Building page image"
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

build-gx:
	@echo "Building great expectations image"
	@docker build -f projects/great-expectations/Dockerfile projects/great-expectations \
	-t gx

run-gx:
	@echo "Running great expectations in container"
	@docker run \
		--rm \
		-v ${GCP_AUTH}:/creds -it \
		-v ${PWD}/projects/great-expectations/:/app \
		--entrypoint /bin/bash \
		-p 8083:8080 \
		gx
