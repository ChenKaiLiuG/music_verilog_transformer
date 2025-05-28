from pathlib import Path

def validate_file(file_path: str, allowed_extensions: list) -> None:
    """
    Validate if the file exists and has an allowed extension.

    Args:
        file_path (str): Path to the file.
        allowed_extensions (list): List of allowed file extensions (e.g., ['.mp3', '.m4a']).

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file extension is not supported.
    """
    if not Path(file_path).is_file():
        raise FileNotFoundError(f"File {file_path} does not exist.")
    if Path(file_path).suffix.lower() not in allowed_extensions:
        raise ValueError(f"Unsupported file format. Allowed: {allowed_extensions}")