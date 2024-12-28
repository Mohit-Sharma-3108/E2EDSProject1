import urllib.request as request
from src.datascience import logger
from src.datascience.entity.config_entity import (DataIngestionconfig)
import zipfile
import os




# This is my DataIngestion component
class DataIngestion:
    def __init__(self, config: DataIngestionconfig):
        self.config = config

    # Downloading zipfile
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        
        else:
            logger.info(f"File already exists")

    # Extracting zipfile
    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory
        Args:
            zip_file_path: str

        Returns:
            None

        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)



