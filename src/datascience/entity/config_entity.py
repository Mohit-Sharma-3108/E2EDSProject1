from dataclasses import dataclass
from pathlib import Path

@dataclass # This decorator let's us create object attributes without using an __init__ function
class DataIngestionconfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path