from sounddevice import Stream
from typing import Optional
import numpy as np

class AudioStream(Stream):
    """
    Stream class to stream live audio data once initialized from user
    """

    # default values
    def __init__(self):

        # Initialise parent stream class
        super().__init__(
            channels = 1,
            samplerate = 41000,
            blocksize = 0,
            callback = self.callback,
            )

    active: bool = False

    def start(self) -> bool:
        super().start()
        self.active = True
        print("Stream started")
        return True

    def stop(self) -> bool:
        super().stop()
        self.active = False
        print("Stream stopped")
        return True


    def callback(self, indata, outdata, frames, time, status):  # TODO sort params
        """Callback function which receives live audio data"""
        if status:
            print(status)
        return indata[:, 0]

# Instantiate the stream
audio_stream = AudioStream()

# Make switch to turn on or off the stream with spacebar
while toggle := input(f"Press <enter> to toggle stream {'on' if audio_stream.active else 'off'}\n"):

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
