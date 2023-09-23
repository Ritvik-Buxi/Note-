import os
import random
import time
import threading
from pydub import AudioSegment
from pydub.playback import play

# Replace this with the path to your directory containing the note files (e.g., C4.wav, D4.wav, etc.).
note_directory = "./"

# List of note filenames
notes = ["C-4.wav", "D-4.wav", "E-4.wav", "F-4.wav", "G-4.wav", "A-4.wav", "B-4.wav"]

# Define the playfile function
def playfile(file):
    sound = AudioSegment.from_file(file, format="wav")
    s = play(sound)
    return s

# Function to play random notes
def play_random_notes():
    while not exit_signal.is_set():
        # Choose a random note from the list
        random_note = random.choice(notes)

        # Construct the full path to the note file
        note_path = os.path.join(note_directory, random_note)

        # Use the playfile function to play the selected note
        playback = playfile(note_path)

        # Pause for a short duration before playing the next note (adjust as needed)
        time.sleep(0.5)  # Adjust the sleep duration to control the note playback speed

# Create a thread for playing random notes
exit_signal = threading.Event()
note_thread = threading.Thread(target=play_random_notes)

# Start the thread
note_thread.start()

# Wait for the user to press Enter to stop
input("Press Enter to stop the music...")

# Set the exit signal to stop the thread
exit_signal.set()

# Wait for the thread to finish
note_thread.join()
