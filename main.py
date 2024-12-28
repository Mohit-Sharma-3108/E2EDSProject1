from src.datascience import logger
from src.datascience.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.pipeline_data_validation import DataValidationTrainingPipeline
from src.datascience.pipeline.pipeline_data_transformation import DataTransformationTrainingPipeline
from src.datascience.pipeline.pipeline_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try: 
    logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>> Stafe {STAGE_NAME} completed! >>>>>\n\nx=========x")

except Exception as e:
    raise e

STAGE_NAME = "Data Validation Stage"

try: 
    logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>> Stafe {STAGE_NAME} completed! >>>>>\n\nx=========x")

except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"

try: 
    logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> Stafe {STAGE_NAME} completed! >>>>>\n\nx=========x")

except Exception as e:
    raise e

STAGE_NAME = "Model Trainer Stage"

try: 
    logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.initiate_model_trainer()
    logger.info(f">>>>> Stage {STAGE_NAME} completed! >>>>>\n\nx=========x")

except Exception as e:
    raise e

