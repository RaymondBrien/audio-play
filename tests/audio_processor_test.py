import pytest
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

from audio_processor import AudioProcessor
from unittest.mock import patch

"""
- Unit tests for audio_processor.py
- Integration tests for combining functions in audio_processor.py
"""

"""
Unit Testing:

Mock the sounddevice library to test read_hertz and play_audio.
Test determine_dominant_pitch_in_hertz with a predefined NumPy array
(mock the audio data).

Test behavior first, then worry about inner workings:
- does class exist
- can it be instantiated
- are the methods callable
- do the methods return the expected results


"""

def test_audio_processor_exists():
    assert AudioProcessor

def test_audio_processor_instantiation():
    audio_processor = AudioProcessor()
    assert audio_processor

def test_audio_processor_record_method():
    audio_processor = AudioProcessor()





"""
Integration Testing:
Test the workflow of recording audio, determining dominant pitch,
and plotting the results (using mocks for hardware dependencies).
"""