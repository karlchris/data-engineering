# Deploying and Running Airflow on Kubernetes

## Quickstart about Kubernetes and DevOps

`Kubernetes` is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

We enter `container deployments era`

### Why you need Kubernetes

Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. 

!!! example

    if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system?

## Deploying Airflow on Kubernetes

- First, you need to clone the repo

```bash
git clone git@github.com:karlchris/airflow-k8s.git
```

- run below command to install the prerequisites, such as: Docker, KinD, Kubectl

```bash
make init
```

it will trigger to install these

```bash
#!/bin/bash

echo "Installing Kubectl, KinD, Helm, docker and docker compose ..."

brew install kubectl
brew install kind
brew install helm
brew install docker
brew install docker-compose

echo "It's ready, you can proceed to install Airflow"
```

### Advantages

### Disadvantages

## References

- [Airflow - Kubernetes Executor](https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/kubernetes_executor.html)

- [KinD](https://kind.sigs.k8s.io/)

- [Helm Chart](https://airflow.apache.org/docs/helm-chart/stable/production-guide.html#webserver-secret-key)

- [Kubectl: Kubernetes CLI](https://kubernetes.io/docs/reference/kubectl/)

- [Airflow on Kubernetes by Marc Lamberti](https://marclamberti.com/blog/airflow-on-kubernetes-get-started-in-10-mins/)
