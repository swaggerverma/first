import pyaudio
import wave

# Set parameters for audio recording
FORMAT = pyaudio.paInt16  # Format of the audio data
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Number of frames per buffer

# Create PyAudio object
audio = pyaudio.PyAudio()

# Open a stream for audio input (microphone)
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Open a WAV file for writing the recorded audio
wf = wave.open("recorded_audio.wav", "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)

# Record audio data in chunks and write to the WAV file
while True:
    data = stream.read(CHUNK)
    wf.writeframes(data)

# Close the stream and PyAudio object
stream.stop_stream()
stream.close()
audio.terminate()

print("Recording finished.")