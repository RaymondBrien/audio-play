from sounddevice import Stream
import numpy as np

class AudioStream(Stream):
    """
    Stream class to stream live audio data once initialized from user
    """

    # default values
    def __init__(self):
        self.active = False
        self.channels = 1
        self.samplerate = 41000

    def start(self):
        self.stream.start()
        self.active = True
        print("Stream started")

    def stop(self):
        self.stream.stop()
        self.active = False
        print("Stream stopped")


# Instantiate the AudioStream class
audio_stream = AudioStream()

# Make switch to turn on or off the stream with spacebar
while toggle := input("Press spacebar to toggle stream on or off: "):
    try:
        match toggle:  # n.b. python@3.10 or higher
            case " ":  # toggle the stream on or off
                if audio_stream.active:
                    audio_stream.stop()
                else:
                    audio_stream.start()
            case _:
                raise ValueError("Please only use the spacebar")
    except KeyboardInterrupt:
        print("Stream stopped")
        break
