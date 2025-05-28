__version__ = '0.1.0'
"""
Audio to MIDI conversion package.
This module provides tools to convert MP3/M4A audio files to MIDI format.
"""

from .audio_loader import load_audio, preprocess_audio
from .pitch_detector import detect_pitches
from .onset_detector import detect_onsets
from .source_separator import separate_sources
from .midi_generator import generate_midi
from .utils import validate_file, clean_temp_files

__all__ = [
    'load_audio',
    'preprocess_audio',
    'detect_pitches',
    'detect_onsets',
    'separate_sources',
    'generate_midi',
    'validate_file',
    'clean_temp_files'
]
