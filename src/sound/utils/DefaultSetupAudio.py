import attr
import logging
import numpy as np
import sounddevice as sd
from typing import Optional

@attr.s(auto_attribs=True)
class DefaultSetupAudio:
    """
    Base class for default values.
    """
    python_version: float = 3.10
    sd_version: str = attr.ib(default=sd.__version__)
    cores: int = 1
    available_devices: dict = {}

    running_test: bool = False
    test_recording_duration: float = 5.0

    recording_active: bool = False
    recorded_audio: list = []
    recording_duration: float = 5.0
    default_samplerate: int = 44100
    default_channels: int = 1

    playing: bool = False
    duration: float = 5.0
    multi_threading: bool = False

    input_device = None
    output_device = None
    blocksize: int = 0

    user_toggle: bool = False # Avoid using input() here
    gui : bool = False
    gui_visible: bool = False
    plot: bool = False
    gui_active: bool = False
    stream: bool = False
    pitch_detection_running: bool = False

    reset: bool = False

    def __name__(self) -> str:
        return str(self.__name__)

    def __repr__(self) -> str:
        return f"DefaultValues: {self.__name__()}"

    def get_available_devices(self) -> dict:
        """Get available input/output devices"""
        self.available_devices = sd.query_devices()
        return dict(self.available_devices)

# Dynamically generate and set the docstring
def generate_doc(cls):
    """
    Generate a docstring for the class based on its attributes.
    """
    doc = cls.__doc__ or ""
    doc += "\n\nAttributes:\n"
    for attribute in attr.fields(cls):
        doc += f"    {attribute.name} ({attribute.type.__name__}): {attribute.default}\n"  # noqa
    return doc

DefaultSetupAudio.__doc__ = generate_doc(DefaultSetupAudio)