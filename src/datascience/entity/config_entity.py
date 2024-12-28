from dataclasses import dataclass
from pathlib import Path

@dataclass # This decorator let's us create object attributes without using an __init__ function
class DataIngestionconfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict # WIll hold schema.yaml's 
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path