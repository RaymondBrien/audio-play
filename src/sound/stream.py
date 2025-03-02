import numpy as np
import curses

from sounddevice import Stream


DIVIDER: str = "\n------------------------------\n------------------------------\n"


class AudioStream(Stream):
    """
    Stream class to stream live audio data once initialized from user
        - NOTE: stdscr must be passed to AudioStream class to work.
        def main(stdscr):
            # Initialize the AudioStream with the stdscr object
            audio_stream = AudioStream(stdscr)
            audio_stream.toggle_stream()

        # Start the curses application required for spacebar interaction
        curses.wrapper(main)
    """
    def __init__(self, stdscr, samplerate=44100, channels=1, blocksize=0):
        active: bool = self.active
        self.stdscr = stdscr # user input in terminal

        # Initialise parent stream class
        super().__init__(
            channels = channels,
            samplerate = samplerate,
            blocksize = blocksize,
            callback = self.callback,
            )

    def start(self) -> bool:
        """Start the audio stream"""
        super().start()
        self.active = True
        print("Stream started")
        return self.active

    def stop(self) -> bool:
        """Stop the audio stream"""
        super().stop()
        self.active = False
        print("Stream stopped")
        return self.active

    def callback(self, indata, outdata, frames, time, status):
        """
        Callback function from sounddevice which receives live audio data

        Args:
            - status (from sounddevice): when true returns self.active = True
            - outdata which processes indata
        """
        if status:
            print(status)
            self.active

        # Process (and modify if needed) indata and write to outdata
        outdata[:] = indata

        # Or if you are only interested in the first channel:
        # outdata[:, 0] = indata[:, 0]


    def toggle_stream(self):
        """
        Helper function to toggle the stream on and off with the spacebar
            - anything other than spacebar will raise a value error
            - this currently relies on curses library to listen for
            keyboard inputs without the need to press enter.
                - In the future this could be improved by making curses
                stdscr optional, so that this class stil works without a UI.

        stdscr will be cleared and status will be shown.
        """
        if not self.stdscr:
            raise ValueError("No curses stdscr provided")

        self.stdscr.clear()
        self.stdscr.addstr(f"Press SPACEBAR to toggle stream {'OFF' if self.active else 'ON'}")
        self.stdscr.refresh()

        while True:
            key = self.stdscr.getch()
            if key == ord(' '):
                if self.active:
                    self.stdscr.addstr(f"{DIVIDER} + STREAM STOPPING" + DIVIDER)
                    self.stdscr.refresh()
                    return self.stop()
                else:
                    self.stdscr.addstr(f"{DIVIDER} + STREAM STOPPING" + DIVIDER)
                    self.stdscr.refresh()
                    return self.start()
            else:
                self.stdscr.addstr("\nPleaseuse the SPACEBAR")
                self.stdscr.refresh()