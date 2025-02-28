from sounddevice import Stream
import numpy as np

class AudioStream(Stream):
    """
    Stream class to stream live audio data once initialized from user
    """

    # default values
    def __init__(self):
        self.active = False
        self.channels = 2  # stereo
        self.samplerate = 41000
        self.blocksize =0  # flexible and variable for optimal performance
        self.dtype = np.int64  # TODO check if this is the right dtype

    def start(self) -> bool:
        self.stream.start()
        self.active = True
        print("Stream started")

    def stop(self) -> bool:
        self.stream.stop()
        self.active = False
        print("Stream stopped")


    def callback(indata, outdata, frames, time, status):  # TODO sort params
        """Callback function which receives live audio data"""
        if status:
            print(status)
        return indata[:, 0]

# Instantiate the stream
audio_stream = AudioStream()
# Make switch to turn on or off the stream with spacebar
while toggle := input("Press spacebar to toggle stream on or off: "):

    try:
        match toggle:  # n.b. python@3.10 or higher
            case " ":  # toggle the stream on or off - TODO use poetry to choose python version
                if audio_stream.active:
                    audio_stream.stop()
                    audio_stream.reset()
                else:
                    audio_stream.start()
            case _:
                raise ValueError("Please only use the spacebar")
    except KeyboardInterrupt:
        print("Stream stopped")
        break
