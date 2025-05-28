import argparse
from src import load_audio, preprocess_audio, detect_pitches, detect_onsets, generate_midi

def main():
    """
    Main function for the audio-to-MIDI CLI.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Convert MP3 or M4A audio files to MIDI format.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help="Path to the input audio file (MP3 or M4A)."
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help="Path to save the output MIDI file (must end with .mid)."
    )
    parser.add_argument(
        '--velocity',
        type=int,
        default=64,
        help="MIDI note velocity (0-127). Default is 64."
    )
    args = parser.parse_args()

    try:
        # Load and preprocess audio
        print(f"Loading audio file: {args.input}")
        waveform, sample_rate = load_audio(args.input)
        waveform, sample_rate = preprocess_audio(waveform, sample_rate)
        print(f"Audio loaded with sample rate: {sample_rate} Hz")

        # Detect pitches
        print("Detecting pitches...")
        pitches = detect_pitches(waveform, sample_rate)

        # Detect onsets
        print("Detecting note onsets...")
        onsets = detect_onsets(waveform, sample_rate)

        # Generate MIDI file
        print(f"Generating MIDI file: {args.output}")
        generate_midi(pitches, onsets, args.output, velocity=args.velocity)
        print(f"MIDI file generated successfully at: {args.output}")

    except (FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
