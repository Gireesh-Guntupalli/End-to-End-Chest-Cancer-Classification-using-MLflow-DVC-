# from src.cnnClassifier import logger
from cnnClassifier import logger  ##logger is in constructer function of cnnClassifier
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# logger.info("Welcome to Cnn Classifier")


STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
