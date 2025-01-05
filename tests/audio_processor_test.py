import pytest
import numpy as np

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

def test_record_method(mocker):
    """Test record method of AudioProcessor class"""

    # arrange
    mock_audio_data = np.random.rand(48000, 1)  # simulate 1 second of audio data

    mocker.patch('sounddevice.rec', return_value=mock_audio_data)
    mocker.patch('sounddevice.wait')  # mock wait call

    audio_processor = AudioProcessor()

    # act
    result = audio_processor.record()

    # assert
    assert isinstance(result, np.ndarray), "Expected a NumPy array"
    # confirm data expected dimensions
    assert result.shape == mock_audio_data.shape, "Expected same shape as mock data"
    np.testing.assert_array_equal(result, mock_audio_data), "Expected same data in mock data and result data"


"""
Integration Testing:
Test the workflow of recording audio, determining dominant pitch,
and plotting the results (using mocks for hardware dependencies).
"""