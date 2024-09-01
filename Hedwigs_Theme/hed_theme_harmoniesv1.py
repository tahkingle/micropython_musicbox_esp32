from machine import Pin, PWM
import time
from note_definitions import parse_melody

# Initialize the PWM objects for the buzzers
buzzer1 = PWM(Pin(5))  # Using GPIO5 for melody
buzzer2 = PWM(Pin(9))  # Using GPIO6 for harmony

buzzer1.duty(0)  # Ensure the first buzzer is silent initially
buzzer2.duty(0)  # Ensure the second buzzer is silent initially

# Set the BPM (tempo)
bpm = 180  # You can change this value to speed up or slow down the melody

# Full melody and harmony for Hedwig's Theme using combined notation
melody = [
    "Q-B3", "Q.-E4", "E-G4", "Q-F#4", "H-E4",
    "Q-B4", "H.-A4", "H.-F#4", 
    "Q.-E4", "E-G4", "Q-F#4", "H-D#4",
    "Q-F4", "H.-B3", "RH", 
    "Q-B3", "Q.-E4", "E-G4", "Q-F#4", "H-E4",
    "Q-B4", "H-D5", "Q-C#5", 
    "H-C5", "Q-A4", "Q.-C5", "E-B4", "H-A#4",
    "Q-F#4", "Q-G4", "H-E4"
]

harmony = [
    "RQ", "H.-E4", "H.-E4", "H.-E4", "H.-E4",
    "H.-E4", "H-A#5", "Q-B3", 
    "H-E4", "Q-G4", "H-B5", "Q-B3",
    "H.-E4", "H.-E4", "H.-A#5", 
    "H.-G#4", "H.-G4", "Q-F4", "Q-E4", "H-D4",
    "H-G4", "H-F#4", "Q-E4", 
    "H-D4", "Q-B3", "H-D4", "Q-C4", "H-G3",
    "H-C4", "H-D4", "Q-B3"
]

# Parse the melodies using the new definitions and adjust for BPM
parsed_melody = parse_melody(melody, bpm)
parsed_harmony = parse_melody(harmony, bpm)

# Print parsed melodies for debugging
print("Parsed Melody:", parsed_melody)
print("Parsed Harmony:", parsed_harmony)

# Function to play the parsed melody and harmony
def play_duet(buzzer1, buzzer2, melody, harmony):
    for (freq1, duration1), (freq2, duration2) in zip(melody, harmony):
        print(f"Playing melody frequency: {freq1} for duration: {duration1}ms")
        print(f"Playing harmony frequency: {freq2} for duration: {duration2}ms")
        
        if freq1 > 0:
            buzzer1.freq(int(freq1))
            buzzer1.duty(512)
        else:
            buzzer1.duty(0)  # Stop the melody tone
        
        if freq2 > 0:
            buzzer2.freq(int(freq2))
            buzzer2.duty(512)
        else:
            buzzer2.duty(0)  # Stop the harmony tone
        
        time.sleep_ms(duration1)  # Wait for the duration of the note/rest
        
        buzzer1.duty(0)  # Stop the melody tone
        buzzer2.duty(0)  # Stop the harmony tone

# Main loop to play the duet
try:
    time.sleep(0.1)  # Small delay before starting the duet
    while True:
        play_duet(buzzer1, buzzer2, parsed_melody, parsed_harmony)
        time.sleep(1)  # Pause for 1 second between repetitions
except KeyboardInterrupt:
    # Silence the buzzers when the program is stopped
    buzzer1.deinit()
    buzzer2.deinit()
    print("Buzzers silenced. Program stopped.")
