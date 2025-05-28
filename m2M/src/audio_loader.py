import os
from pathlib import Path
import numpy as np
from pydub import AudioSegment
import librosa
from .utils import validate_file

def load_audio(file_path: str) -> tuple[np.ndarray, float]:
    """
    Load an audio file (MP3 or M4A) and convert it to a waveform.

    Args:
        file_path (str): Path to the input audio file.

    Returns:
        tuple: (waveform, sample_rate) where waveform is a numpy array and sample_rate is a float.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the file format is not supported.
    """
    # Validate file
    validate_file(file_path, allowed_extensions=['.mp3', '.m4a'])

    # Load audio using pydub
    try:
        audio = AudioSegment.from_file(file_path)
        # Export to temporary WAV file for librosa
        temp_wav = "temp_audio.wav"
        audio.export(temp_wav, format="wav")
        
        # Load waveform and sample rate using librosa
        waveform, sample_rate = librosa.load(temp_wav, sr=None)
        
        # Clean up temporary file
        if os.path.exists(temp_wav):
            os.remove(temp_wav)
            
        return waveform, sample_rate
    except Exception as e:
        raise RuntimeError(f"Failed to load audio file {file_path}: {str(e)}")

def preprocess_audio(waveform: np.ndarray, sample_rate: float) -> tuple[np.ndarray, float]:
    """
    Preprocess the audio waveform for MIDI conversion.

    Args:
        waveform (np.ndarray): Input audio waveform.
        sample_rate (float): Sample rate of the audio.

    Returns:
        tuple: (processed_waveform, sample_rate) where processed_waveform is normalized and mono.
    """
    # Convert to mono if stereo
    if waveform.ndim > 1:
        waveform = librosa.to_mono(waveform)
    
    # Normalize audio to [-1, 1]
    if np.max(np.abs(waveform)) > 0:
        waveform = waveform / np.max(np.abs(waveform))
    
    return waveform, sample_rate
