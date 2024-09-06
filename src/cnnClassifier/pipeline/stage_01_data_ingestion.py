from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = (
                ConfigurationManager()
            )  ##revoking constructor from entity ConfigurationManager
            data_ingestion_config = (
                config.get_data_ingestion_config()
            )  ##config.yaml is connected
            data_ingestion = DataIngestion(
                config=data_ingestion_config
            )  ## componed instance
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
