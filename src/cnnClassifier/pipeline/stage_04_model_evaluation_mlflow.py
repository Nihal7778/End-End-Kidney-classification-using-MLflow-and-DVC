from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger
import mlflow, dagshub
import os
from dotenv import load_dotenv

import tensorflow as tf
tf.keras.__version__ = tf.__version__ # type: ignore

load_dotenv()

dagshub.init(repo_owner='Nihal7778', repo_name='End-End-Kidney-classification-using-MLflow-and-DVC', mlflow=True)

mlflow_username = os.getenv("MLFLOW_TRACKING_USERNAME")
mlflow_password = os.getenv("MLFLOW_TRACKING_PASSWORD")

if not mlflow_username or not mlflow_password:
    raise ValueError("Set MLFLOW_TRACKING_USERNAME and MLFLOW_TRACKING_PASSWORD in .env")

os.environ["MLFLOW_TRACKING_USERNAME"] = mlflow_username
os.environ["MLFLOW_TRACKING_PASSWORD"] = mlflow_password

# Set tracking URI
mlflow.set_tracking_uri("https://dagshub.com/Nihal7778/End-End-Kidney-classification-using-MLflow-and-DVC.mlflow")

# Create or get experiment
experiment_name = "kidney-classification-v2"
try:
    mlflow.create_experiment(experiment_name)
except Exception:
    pass

mlflow.set_experiment(experiment_name)

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self) -> None:
        pass
        
        
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
