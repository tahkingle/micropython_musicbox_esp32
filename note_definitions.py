import math

# Frequency to Note Conversion Function
def frequency_to_note(frequency):
    # Define constants
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    OCTAVE_MULTIPLIER = 2
    KNOWN_NOTE_NAME, KNOWN_NOTE_OCTAVE, KNOWN_NOTE_FREQUENCY = ('A', 4, 440)
    
    # Calculate distance from known note
    note_multiplier = OCTAVE_MULTIPLIER ** (1 / len(NOTES))
    frequency_relative_to_known_note = frequency / KNOWN_NOTE_FREQUENCY
    distance_from_known_note = math.log(frequency_relative_to_known_note, note_multiplier)
    distance_from_known_note = round(distance_from_known_note)
    
    # Calculate note name and octave
    known_note_index_in_octave = NOTES.index(KNOWN_NOTE_NAME)
    known_note_absolute_index = KNOWN_NOTE_OCTAVE * len(NOTES) + known_note_index_in_octave
    note_absolute_index = known_note_absolute_index + distance_from_known_note
    note_octave, note_index_in_octave = note_absolute_index // len(NOTES), note_absolute_index % len(NOTES)
    note_name = NOTES[note_index_in_octave]
    return (note_name, note_octave)

# Note to Frequency Conversion Function
def note_to_frequency(note_name, octave):
    NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    OCTAVE_MULTIPLIER = 2
    KNOWN_NOTE_NAME, KNOWN_NOTE_OCTAVE, KNOWN_NOTE_FREQUENCY = ('A', 4, 440)
    
    known_note_index_in_octave = NOTES.index(KNOWN_NOTE_NAME)
    known_note_absolute_index = KNOWN_NOTE_OCTAVE * len(NOTES) + known_note_index_in_octave
    note_absolute_index = octave * len(NOTES) + NOTES.index(note_name)
    distance_from_known_note = note_absolute_index - known_note_absolute_index
    
    frequency = KNOWN_NOTE_FREQUENCY * (OCTAVE_MULTIPLIER ** (distance_from_known_note / len(NOTES)))
    return frequency

# Rhythm Durations and Rest Durations Based on Combined Format
durations = {
    'W': 4.0,  # Whole note (4 beats)
    'H': 2.0,  # Half note (2 beats)
    'Q': 1.0,  # Quarter note (1 beat)
    'E': 0.5,  # Eighth note (0.5 beats)
    'S': 0.25, # Sixteenth note (0.25 beats)
    'T': 0.125, # Thirty-second note (0.125 beats)
    'W.': 6.0, # Dotted whole note (6 beats)
    'H.': 3.0, # Dotted half note (3 beats)
    'Q.': 1.5, # Dotted quarter note (1.5 beats)
    'E.': 0.75, # Dotted eighth note (0.75 beats)
    'S.': 0.375, # Dotted sixteenth note (0.375 beats)
    'T.': 0.1875, # Dotted thirty-second note (0.1875 beats)
    'RS': 0.25, # Sixteenth rest (0.25 beats)
    'RE': 0.5, # Eighth rest (0.5 beats)
    'RQ': 1.0, # Quarter rest (1 beat)
    'RH': 2.0, # Half rest (2 beats)
    'RW': 4.0, # Whole rest (4 beats)
    'RT': 0.125, # Thirty-second rest (0.125 beats)
    'RS.': 0.375, # Dotted sixteenth rest (0.375 beats)
    'RE.': 0.75, # Dotted eighth rest (0.75 beats)
    'RQ.': 1.5, # Dotted quarter rest (1.5 beats)
    'RH.': 3.0, # Dotted half rest (3 beats)
    'RW.': 6.0, # Dotted whole rest (6 beats)
}

# Function to parse the combined notation
def parse_melody(melody, bpm=120):
    parsed_melody = []
    for item in melody:
        try:
            if item.startswith('R'):  # Handle rests
                rhythm = item
                duration = int(durations[rhythm] * 60000 / bpm)  # Convert to ms
                parsed_melody.append((0, duration))
            else:  # Handle notes
                rhythm, note = item.split('-')
                
                # Debugging prints
                print(f"Processing: rhythm='{rhythm}', note='{note}'")

                # Ensure that the last character is a digit (octave)
                octave = note[-1]
                if not octave.isdigit():
                    raise ValueError(f"Invalid octave: '{octave}' in note '{note}'")

                # Convert the note duration and frequency
                duration = int(durations[rhythm] * 60000 / bpm)  # Convert to ms
                frequency = note_to_frequency(note[:-1], int(octave))
                parsed_melody.append((frequency, duration))
        except Exception as e:
            print(f"Error processing '{item}': {e}")
            raise
    return parsed_melody


