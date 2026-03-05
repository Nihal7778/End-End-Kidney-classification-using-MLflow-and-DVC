# End-to-End Chicken Coccidiosis Classification Using VGG16, MLflow, and DVC

- A production ready deep learning pipeline that classifies chicken fecal images as Coccidiosis (infected) or Healthy using a fine tuned VGG16 model. The project demonstrates end to end MLOps practices with MLflow for experiment tracking and DVC for pipeline orchestration and data versioning.

## Workflows

```bash

1.Update config.yaml
2.Update params.yaml
3.Update the entity
4.Update the configuration manager in src config
5.Update the components
6.Update the pipeline
7.Update the main.py
8.Update dvc.yaml
9.Update the app.py

```

## Overview

- Coccidiosis is a parasitic disease affecting poultry that leads to significant economic losses in the farming industry. Early detection through automated image classification can help farmers take timely action. This project builds a complete ML pipeline — from data ingestion to a deployable Flask web application — following software engineering and MLOps best practices.

- Key highlights:

- Transfer learning with VGG16 (ImageNet weights)
- Configurable training via config.yaml and params.yaml
- Experiment tracking and model logging with MLflow + DagsHub
- Reproducible pipelines with DVC
- Flask API with a drag-and-drop image upload UI for inference




## Tech Stack
CategoryToolsDeep LearningTensorFlow / Keras, VGG16Experiment TrackingMLflow, DagsHubPipeline OrchestrationDVCWeb FrameworkFlaskLanguagePython 3.8EnvironmentConda (mlops-env)

## Project Structure
├── .dvc/                       # DVC configuration
├── .github/workflows/          # CI/CD workflows
├── config/
│   └── config.yaml             # Paths, URLs, and model configuration
├── research/                   # Jupyter notebooks (experimentation)
├── src/cnnClassifier/
│   ├── components/             # Data ingestion, model training, evaluation
│   ├── config/                 # ConfigurationManager
│   ├── constants/              # Project root & path constants
│   ├── entity/                 # Dataclass config entities
│   ├── pipeline/               # Stage runners & prediction pipeline
│   └── utils/                  # Common utilities
├── templates/                  # Flask HTML templates
├── app.py                      # Flask application entry point
├── main.py                     # Pipeline orchestrator (all stages)
├── params.yaml                 # Hyperparameters (epochs, batch size, LR, image size)
├── dvc.yaml                    # DVC pipeline definition
├── dvc.lock                    # DVC lock file
├── scores.json                 # Evaluation metrics output
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
└── template.py                 # Project scaffolding script

## Pipeline Stages
- StageDescriptionData IngestionDownloads and extracts the chicken fecal image datasetBase Model PreparationLoads VGG16 with ImageNet weights and prepares a custom classification headModel TrainingFine-tunes the model on the training set with configurable hyperparametersModel EvaluationEvaluates on the test set, logs metrics and the model to MLflow

## Getting Started
1. Clone the repository
bashgit clone https://github.com/Nihal7778/End-to-End-Chicken-Coccidiosis-Classification-Using-VGG16-MLflow-and-DVC.git
cd End-to-End-Chicken-Coccidiosis-Classification-Using-VGG16-MLflow-and-DVC
2. Create and activate a conda environment
bashconda create -n mlops-env python=3.8 -y
conda activate mlops-env
3. Install dependencies
bashpip install -r requirements.txt
4. Run the full pipeline
bashpython main.py
This executes all four stages sequentially: data ingestion → base model preparation → training → evaluation.

## MLflow Experiment Tracking
- Experiments are tracked on DagsHub. Set the following environment variables before running the pipeline:
- bashexport MLFLOW_TRACKING_URI=https://dagshub.com/Nihal7778/End-to-End-Chicken-Coccidiosis-Classification-Using-VGG16-MLflow-and-DVC.mlflow
- export MLFLOW_TRACKING_USERNAME=Nihal7778
- export MLFLOW_TRACKING_PASSWORD=<your_dagshub_token>
- Metrics logged include test loss and test accuracy. The trained model is also registered as an MLflow artifact.

## DVC Pipeline
DVC manages pipeline reproducibility and data versioning.
bash# Initialize DVC (first time only)
dvc init

# Reproduce the full pipeline
- dvc repro

# View the pipeline DAG
- dvc dag
- The pipeline stages are defined in dvc.yaml with dependencies and outputs for each step, ensuring that only stages with changed inputs are re executed.

## Flask Web App
- The project includes a Flask application for real-time inference.
- bashpython app.py
- Navigate to http://localhost:8080 in your browser. Upload a chicken fecal image, and the app will return a prediction of Coccidiosis or Healthy.
- The prediction pipeline handles base64 image decoding, preprocessing (resizing to 224×224 and normalizing pixel values to [0, 1]), and inference using the trained model.

## DVC commands

```bash

1.dvc.init
2.dvc.repro
3.dvc.dag

```

