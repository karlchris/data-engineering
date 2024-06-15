MKDM_VERSION=9.5.24
PWD=`pwd`
PORT=8000
IMG=de-kchrs
USER := `whoami | tr . _`


stop:
	@docker stop ${IMG}

# Build docker image for local development
build-page:
	@echo "Building page image"
	@docker build . -f Dockerfile \
		-t ${IMG}:dev \
		--build-arg MKDM_VERSION=${MKDM_VERSION}

# Run dev server in docker
dev: build-page
	@echo "Starting dev server in a docker container"
	@docker run \
		--rm -d \
		--name ${IMG} \
		-p 127.0.0.1:${PORT}:8000 \
		-v ${PWD}:/docs \
		${IMG}:dev
	@echo "http://localhost:8000 is ready"

test:
	@docker build . -f Dockerfile-test \
		-t ${IMG}:test
	@docker run --rm  --name ${IMG}-test ${IMG}:test
