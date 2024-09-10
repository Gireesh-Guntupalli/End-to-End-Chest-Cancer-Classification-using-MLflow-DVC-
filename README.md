# End-to-End Deep Learning Project Implementation using MLOps Tool (MLflow & DVC) with CI/CD Deployment

## Overview

This project focuses on developing an end-to-end pipeline for chest cancer CT scan classification using transfer learning. The model is built using the VGG16 architecture with pretrained weights and a custom classifier for predicting cancer from CT scan images. The project also integrates MLOps tools, such as MLflow for experiment tracking and DVC for version control, to ensure a smooth workflow, reproducibility, and CI/CD deployment on AWS EC2.

## Table of Contents
- [Project Architecture](#project-architecture)
- [Workflows](#work-flows)
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

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update entity
5. Update configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update dvc.yaml

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
 
  
## MLflow:
<img width="937" alt="image" src="https://github.com/user-attachments/assets/cab9bb27-b3ee-4b5e-909c-09b8b3625d9a">
<img width="943" alt="image" src="https://github.com/user-attachments/assets/e230a81f-4fa4-476e-b8c7-ef3e2f363dfb">

## DVC
<img width="733" alt="image" src="https://github.com/user-attachments/assets/ed7c2595-c547-46c1-976a-d96755d7dc3b">


Install the required packages using:

```bash
pip install -r requirements.txt
