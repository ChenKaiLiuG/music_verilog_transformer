from pathlib import Path
import os
from typing import List

def validate_file(file_path: str, allowed_extensions: List[str]) -> None:
    """
    Validate if the file exists and has an allowed extension.

    Args:
        file_path (str): Path to the file.
        allowed_extensions (List[str]): List of allowed file extensions (e.g., ['.mp3', '.m4a']).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file extension is not supported.
    """
    file_path = str(file_path).strip()
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"File {file_path} does not exist.")
    if Path(file_path).suffix.lower() not in [ext.lower() for ext in allowed_extensions]:
        raise ValueError(f"Unsupported file format: {Path(file_path).suffix}. Allowed: {allowed_extensions}")

def clean_temp_files(temp_files: List[str] = None) -> None:
    """
    Remove temporary files created during processing.

    Args:
        temp_files (List[str], optional): List of temporary file paths to delete.
                                         If None, removes all .wav files in the current directory.

    Raises:
        RuntimeError: If a file cannot be deleted.
    """
    if temp_files is None:
        temp_files = [f for f in os.listdir('.') if f.endswith('.wav')]
    
    for file_path in temp_files:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            raise RuntimeError(f"Failed to delete temporary file {file_path}: {str(e)}")
