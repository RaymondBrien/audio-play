import sounddevice as sd
import numpy as np

class DefaultSetupAudio:
    """
    Base class for default values
    """

    def __init__(self):
        """Initial setup of default values"""
        self.python.version = 3.10
        self.sd.version = sd.__version__

        self.cores : int = 1
        self.available_devices = None

        # manual test params
        self.running_test : bool = False
        self.test_duration : float = 5.0

        # recording params
        self.recording : bool = False
        self.recorded_audio : np.array = None
        self.recording_duration : float = 5.0

        self.default_samplerate = sd.default.samplerate = 44100
        self.default_channels = sd.default.channels = 1

        self.playing : bool = False
        self.duration : float = 5.0

        self.test_recording_duration : float = 5.0

        self.multi_threading : bool = False
        self.input_device : bool = None
        self.output_device : bool = None

        self.blocksize : int = 0
        self.dtype = np.int64

        # visuals
        self.input = input()
        self.gui_visible : bool = False
        self.gui : bool = None
        self.plot : bool = False
        self.gui_active : bool = False

        # stream
        self.stream = None

        # audio processor
        self.pitch_detection_running : bool = False

        # reset
        self.reset = False

    def __name__(self) -> str:
        return str(self.__name__)

    def __repr__(self) -> str:
        return f"DefaultValues: {self.__name__()}"

    def get_available_devices(self) -> dict:
        """Get available input/output devices"""
        self.available_devices = sd.query_devices()
        return self.available_devices
