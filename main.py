from src.datascience import logger
from src.datascience.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> Stafe {STAGE_NAME} completed! >>>>>\n\nx=========x")

except Exception as e:
    raise e

