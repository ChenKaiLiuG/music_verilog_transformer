import numpy as np
import librosa

def detect_pitches(waveform: np.ndarray, sample_rate: float, frame_size: int = 2048, hop_size: int = 512) -> list[tuple[float, int]]:
    """
    Detect pitches from an audio waveform and convert them to MIDI note values.

    Args:
        waveform (np.ndarray): Input audio waveform (mono).
        sample_rate (float): Sample rate of the audio.
        frame_size (int): Size of the FFT window for pitch detection (default: 2048).
        hop_size (int): Hop size for frame-by-frame analysis (default: 512).

    Returns:
        list[tuple[float, int]]: List of (time, midi_note) pairs, where time is in seconds and midi_note is an integer.

    Raises:
        ValueError: If waveform is empty or invalid.
    """
    # Validate input
    if not isinstance(waveform, np.ndarray) or waveform.size == 0:
        raise ValueError("Invalid waveform: empty or not a numpy array.")
    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")

    # Use pyin algorithm for pitch detection
    try:
        f0, voiced_flag, voiced_probs = librosa.pyin(
            y=waveform,
            fmin=librosa.note_to_hz('C2'),  # Minimum frequency (C2 ~ 65 Hz)
            fmax=librosa.note_to_hz('C7'),  # Maximum frequency (C7 ~ 2093 Hz)
            sr=sample_rate,
            frame_length=frame_size,
            hop_length=hop_size,
            center=True
        )
    except Exception as e:
        raise RuntimeError(f"Pitch detection failed: {str(e)}")

    # Convert detected frequencies to MIDI notes
    pitches = []
    for i, (freq, voiced) in enumerate(zip(f0, voiced_flag)):
        if voiced and not np.isnan(freq):
            midi_note = int(round(librosa.hz_to_midi(freq)))
            time = i * hop_size / sample_rate  # Convert frame index to seconds
            pitches.append((time, midi_note))

    return pitches
