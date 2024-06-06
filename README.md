# Data Engineering Handbook

This is my public Repository about Data Engineering.

To run and test this locally (please make sure you have [Docker](https://docs.docker.com/engine/install/)), run

```bash
make build-page
```

it will build the docker image locally.

Then, run

```bash
make dev
```

it will run the docker image and expose the UI to `http://localhost:8000/data-engineering/`.

## Lint files and test it out

```bash
make test
```

## Clean up

run this command

```bash
make clean
```
