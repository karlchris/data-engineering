MKDM_VERSION=9.5.24
PWD=`pwd`
PORT=8000
IMG=learn-de-kchrs


# Build docker image for local development
build-docker:
	@docker build . -f Dockerfile \
		-t ${IMG}:dev \
		--build-arg MKDM_VERSION=${MKDM_VERSION}

# Run dev server in docker
dev:
	echo "Starting dev server in a docker container"
	@docker run \
		--rm -it \
		-p 127.0.0.1:${PORT}:8000 \
		-v ${PWD}:/docs \
		${IMG}:dev
