import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml files and return COnfigBox

    Args:
        path_to_yaml(str): Path like input
    
    Raises:
        ValueError: If yaml file is empty
        e: Empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): List of path directories
        ignore_log (bool, optional): Ignore if multiple dirs are to be created. Defaults to True
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data

    Args:
        path(Path): Path to json file
        data(dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"Json file saved at: {path}")

@ensure_annotations
def load_json(path: Path):
    """
    Load json file's data

    Args:
        path(Path): Path to json file
        
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"Json file loaded successfully from: {path}")

    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary file

    Args:
        data (Any): Data to be saved as a binary file
        path (Path): Path where binary file has to be saved
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path):
    """
    Load binary file

    Args:
        path (Path): Path to binary file
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")

    return data

