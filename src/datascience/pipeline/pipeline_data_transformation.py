from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger

from pathlib import Path


STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            data_validation_status_txt_path = r"C:\Users\Mohit\Desktop\Mohit\Projects\E2EDSProject1\artifacts\data_validation\status.txt"
            # This below code is to ensure that the data transformation step is performed only when 
            # the status.txt file has all True for each row
            with open(data_validation_status_txt_path, "r") as f:
                lines = f.readlines()

                for line in lines:
                    if not line.strip().endswith("True"):
                        raise ValueError(f"Validation failed for line: {line}")
                
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            

        except FileNotFoundError:
            print("Status.txt file not found")

        except Exception as e:
            logger.exception(e)
            raise e


        


if __name__ == "__main__":
    try: 
        logger.info(f">>>>> Stage: {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> Stafe {STAGE_NAME} completed! >>>>>\n\nx=========x")

    except Exception as e:
        raise e