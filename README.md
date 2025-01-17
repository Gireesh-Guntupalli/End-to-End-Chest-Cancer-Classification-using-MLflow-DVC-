# End-to-End Deep Learning Project Implementation using MLOps Tool (MLflow & DVC) with CI/CD Deployment

## Overview

This project focuses on developing an end-to-end pipeline for chest cancer CT scan classification using transfer learning. The model is built using the VGG16 architecture with pretrained weights and a custom classifier for predicting cancer from CT scan images. The project also integrates MLOps tools, such as MLflow for experiment tracking and DVC for version control, to ensure a smooth workflow, reproducibility, and CI/CD deployment on AWS EC2.

## Table of Contents
- [Project Architecture](#project-architecture)
- [Workflows](#workflows)
- [Model Details](#model-details)
- [Pipelines](#pipelines)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Model Training](#model-training)
- [Experiment Tracking with MLflow](#experiment-tracking-with-mlflow)
- [DVC for Version Control](#dvc-for-version-control)
- [Prediction Interface](#prediction-interface)
- [CI/CD Deployment](#cicd-deployment)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Architecture
#### DVC dag
<img width="733" alt="image" src="https://github.com/user-attachments/assets/ed7c2595-c547-46c1-976a-d96755d7dc3b">

## Workflows 

1. **Update `config.yaml`**: Modify the configuration settings such as paths, model parameters, and environment-specific variables.
2. **Update `secrets.yaml` [Optional]**: If you use secret credentials or keys, update them here.
3. **Update `params.yaml`**: This file contains hyperparameters and experiment-specific settings that drive the training process.
4. **Update the Entity**: Define or update entities (classes, models, and functions) in the relevant files under the `src` folder.
5. **Update the Configuration Manager in `src/config`**: Ensure that configuration files are loaded and passed correctly across modules.
6. **Update the Components**: Modify the existing components (e.g., data ingestion, model training, evaluation, prediction) to fit new requirements.
7. **Update the Pipeline**: Adjust pipeline stages in DVC, making sure all dependencies are well-defined.
8. **Update `main.py`**: Integrate all updates in the main entry script that triggers the end-to-end pipeline.
9. **Update `dvc.yaml`**: Ensure that the DVC pipeline reflects the correct order of execution for each stage.

## Model Details

- **Base Model**: VGG16 (Pretrained on ImageNet)
- **Frozen Layers**: All convolutional layers are frozen to retain learned features from ImageNet.
- **Custom Classifier**: Added custom dense layers for the chest cancer classification task.
- **Optimizer**: Adam
- **Loss Function**: Categorical Cross-Entropy

  
## Pipelines

This project is structured into 5 pipelines:

1. **Data Ingestion**:
   - Ingests the raw CT scan images and labels.
   - Handles data preprocessing and augmentation.

2. **Base Model Preparation**:
   - Loads the pretrained VGG16 model and adds custom dense layers.
   - Freezes convolutional layers and compiles the model.

3. **Model Training**:
   - Trains the model using the preprocessed data.
   - Tracks the training process using MLflow.

4. **Model Evaluation**:
   - Evaluates the model on a validation dataset.
   - Logs accuracy, precision, recall, and other metrics using MLflow.

5. **Prediction Pipeline**:
   - Performs predictions on unseen images.
   - Provides a simple Flask interface for users to upload images and get predictions.

## Technologies Used

- **Deep Learning**: TensorFlow, Keras
- **MLOps Tools**:
  - **MLflow**: Used for experiment tracking, logging metrics, and model versioning.
  - **DVC**: Used for data version control and pipeline management.
- **CI/CD Deployment**:
  - **Flask**: Used for the web interface to handle image uploads and display predictions.
  - **Docker**: Used for containerization of the app.
  - **AWS EC2**: Used for deployment of the Flask app with continuous integration and delivery.
 
## Prerequisites

	Install the required packages using:
	
	```bash
	pip install -r requirements.txt


## Experiment Tracking with MLflow  
## MLflow:

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

##### Sanpshots from MLflow ui
<img width="937" alt="image" src="https://github.com/user-attachments/assets/cab9bb27-b3ee-4b5e-909c-09b8b3625d9a">
<img width="943" alt="image" src="https://github.com/user-attachments/assets/e230a81f-4fa4-476e-b8c7-ef3e2f363dfb">\


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

## CI/CD Deployment
### CI/CD Pipeline with GitHub Actions, all about main.yaml file

This repository contains a GitHub Actions workflow configuration for automating a **CI/CD (Continuous Integration and Continuous Delivery/Deployment)** pipeline. The pipeline ensures that code is automatically tested, built, and deployed using **Docker** and **Amazon Elastic Container Registry (ECR)**.

### Workflow Overview

The GitHub Actions workflow is defined in the `main.yaml` file. It performs the following key tasks:

#### 1. Continuous Integration (CI)
Ensures that the codebase is linted and tested before proceeding to deployment.

- **Triggered**: When code is pushed to the `main` branch (excluding changes to `README.md`).
- **Steps**:
  - **Checkout Code**: Pulls the latest code from the repository.
  - **Lint Code**: Runs linting to check for code quality issues.
  - **Run Unit Tests**: Executes unit tests to validate the code.

#### 2. Continuous Delivery (CD)
Builds and pushes the application as a Docker image to **Amazon ECR** after the code passes the CI phase.

- **Steps**:
  - **Checkout Code**: Pulls the latest code from the repository.
  - **Install Utilities**: Installs necessary tools (e.g., `jq`, `unzip`).
  - **Configure AWS Credentials**: Uses AWS credentials stored as GitHub Secrets to authenticate with AWS services.
  - **Login to Amazon ECR**: Authenticates to Amazon ECR using AWS credentials.
  - **Build and Push Docker Image**: Builds a Docker image from the repository and pushes it to Amazon ECR.

#### 3. Continuous Deployment (CD)
Deploys the Docker image from Amazon ECR to a self-hosted environment.

- **Steps**:
  - **Checkout Code**: Pulls the latest code from the repository.
  - **Configure AWS Credentials**: Authenticates with AWS to access the ECR registry.
  - **Login to Amazon ECR**: Logs in to the Amazon ECR Docker registry.
  - **Pull Latest Docker Image**: Pulls the latest Docker image from ECR.
  - **Run Docker Container**: Starts the application by running the Docker image on the server.
  - **Clean Up**: Cleans up unused Docker images and containers to free up resources.

### AWS Integration

This workflow uses **AWS** services, including:
- **Amazon Elastic Container Registry (ECR)**: To store Docker images.
- **AWS Credentials**: Configured using GitHub Secrets to securely authenticate with AWS services.

#### Secrets Required
The following secrets must be added to the GitHub repository for the workflow to function:
- `AWS_ACCESS_KEY_ID`: AWS access key for authentication.
- `AWS_SECRET_ACCESS_KEY`: AWS secret key for authentication.
- `AWS_REGION`: AWS region where the services are hosted.
- `ECR_REPOSITORY_NAME`: Name of the Amazon ECR repository.

### Prerequisites

- AWS account with permissions to use ECR.
- Docker installed on the self-hosted runner for deployment.

### Conclusion of CI/CD 

This pipeline automates the process of:
1. **Testing**: Ensuring code quality through linting and unit tests.
2. **Building**: Creating a Docker image of the application.
3. **Pushing**: Uploading the Docker image to Amazon ECR.
4. **Deploying**: Running the Docker image on a server to make the application live.

With this setup, code can be automatically tested, built, and deployed with minimal manual intervention, streamlining the development and deployment process.


### AWS-CICD-Deployment-with-Github-Actions in detail

#### 1. Login to AWS console.

#### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
#### 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
#### 4. Create EC2 machine (Ubuntu) 

#### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
#### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


#### 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




