import numpy as np
import librosa

def detect_onsets(waveform: np.ndarray, sample_rate: float, frame_size: int = 2048, hop_size: int = 512) -> list[tuple[float, float]]:
    """
    Detect note onsets and durations from an audio waveform.

    Args:
        waveform (np.ndarray): Input audio waveform (mono).
        sample_rate (float): Sample rate of the audio.
        frame_size (int): Size of the analysis window (default: 2048).
        hop_size (int): Hop size for frame-by-frame analysis (default: 512).

    Returns:
        list[tuple[float, float]]: List of (onset_time, duration) pairs, where onset_time and duration are in seconds.

    Raises:
        ValueError: If waveform is empty or invalid.
    """
    # Validate input
    if not isinstance(waveform, np.ndarray) or waveform.size == 0:
        raise ValueError("Invalid waveform: empty or not a numpy array.")
    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")

    try:
        # Detect onsets using librosa's onset detection
        onset_frames = librosa.onset.onset_detect(
            y=waveform,
            sr=sample_rate,
            hop_length=hop_size,
            frame_length=frame_size,
            backtrack=True,  # Improve onset timing accuracy
            units='frames'
        )
        
        # Convert frame indices to time (seconds)
        onset_times = librosa.frames_to_time(onset_frames, sr=sample_rate, hop_length=hop_size)
        
        # Estimate durations (simple approach: duration is time to next onset or end of audio)
        durations = []
        audio_duration = len(waveform) / sample_rate
        for i, onset in enumerate(onset_times):
            if i < len(onset_times) - 1:
                duration = onset_times[i + 1] - onset
            else:
                duration = audio_duration - onset
            durations.append(duration)
        
        # Filter out unreasonably short durations (e.g., < 10ms)
        min_duration = 0.01  # 10ms
        valid_onsets = [(t, d) for t, d in zip(onset_times, durations) if d >= min_duration]
        
        return valid_onsets
    except Exception as e:
        raise RuntimeError(f"Onset detection failed: {str(e)}")
