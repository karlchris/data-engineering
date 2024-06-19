# Building Machine Learning Pipeline using MLflow on Kubernetes

We will cover an end-to-end model development process including model training and testing within this tiny project, using MLflow and deployed on Kubernetes.

## About MLflow

Stepping into the world of Machine Learning is an exciting journey, but it often comes with complexities that can hinder innovation and experimentation.

**MLflow** is a solution to many of these issues in this dynamic landscape, offering tools and simplifying processes to streamline the ML lifecycle and foster collaboration among ML practitioners.

MLflow, at its core, provides a suite of tools aimed at simplifying the ML workflow. It is tailored to assist ML practitioners throughout the various stages of ML development and deployment.

### Core Components

![mlflow-architecture](pics/mlflow-architecture.png)

### Why use MLflow?

### Use Cases

### Scalability

## Quick Start

This quick start demonstrates how to use MLflow end-to-end for:

- Training a linear regression model with MLflow Tracking.
- Conducting hyper-parameter tuning to find the best model.
- Packaging the model weights and dependencies as an MLflow Model.
- Testing model serving locally with mlserver using the mlflow models serve command.
- Deploying the model to a Kubernetes cluster using KServe with MLflow.

### Introduction: Model Serving with KServe and MLServer

#### What is KServe?

#### Benefits

### 1. Installing MLflow and dependencies

### 2. Setting up Kubernetes Kind Cluster

### 3. Training the Model

### 4. Running Hyperparameter Tuning

### 5. Packaging the Model

### 6. Testing Model Serving Locally

### 7. Deploying the Model to KServe

### 8. Test Request to the Server

### Clean up cluster

## References

- [Official MLflow Documentation](https://mlflow.org/docs/latest/introduction/index.html)
