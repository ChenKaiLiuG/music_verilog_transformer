from typing import List, Tuple
import mido
from mido import MidiFile, MidiTrack, Message

def generate_midi(pitches: List[Tuple[float, int]], onsets: List[Tuple[float, float]], output_path: str, velocity: int = 64) -> None:
    """
    Generate a MIDI file from detected pitches and onsets.

    Args:
        pitches (List[Tuple[float, int]]): List of (time, midi_note) pairs, where time is in seconds.
        onsets (List[Tuple[float, float]]): List of (onset_time, duration) pairs, where times are in seconds.
        output_path (str): Path to save the output MIDI file.
        velocity (int): MIDI velocity (volume) for notes, default is 64 (range: 0-127).

    Raises:
        ValueError: If inputs are invalid or empty.
        RuntimeError: If MIDI file creation fails.
    """
    # Validate inputs
    if not pitches or not onsets:
        raise ValueError("Pitches or onsets list is empty.")
    if not isinstance(pitches, list) or not isinstance(onsets, list):
        raise ValueError("Pitches and onsets must be lists of tuples.")
    if not output_path.endswith('.mid'):
        raise ValueError("Output file must have .mid extension.")
    if not (0 <= velocity <= 127):
        raise ValueError("Velocity must be between 0 and 127.")

    try:
        # Create MIDI file and track
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        # Align pitches with onsets
        midi_events = []
        for onset, duration in onsets:
            # Find the closest pitch to this onset time
            closest_pitch = min(pitches, key=lambda x: abs(x[0] - onset), default=(0, 60))
            midi_note = closest_pitch[1]
            # Ensure MIDI note is within valid range (0-127)
            if 0 <= midi_note <= 127:
                midi_events.append((onset, duration, midi_note))

        # Sort events by onset time
        midi_events.sort(key=lambda x: x[0])

        # Convert to MIDI time (ticks, assuming 500 ticks per second)
        ticks_per_second = 500
        previous_time = 0
        for onset, duration, midi_note in midi_events:
            # Calculate time delta in ticks
            delta_time = int((onset - previous_time) * ticks_per_second)
            # Add note_on event
            track.append(Message('note_on', note=midi_note, velocity=velocity, time=delta_time))
            # Add note_off event
            track.append(Message('note_off', note=midi_note, velocity=velocity, time=int(duration * ticks_per_second)))
            previous_time = onset + duration

        # Save MIDI file
        mid.save(output_path)
    except Exception as e:
        raise RuntimeError(f"Failed to generate MIDI file: {str(e)}")
