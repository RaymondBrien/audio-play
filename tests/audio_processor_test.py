import pytest
import numpy as np

from audio_processor import AudioProcessor

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

def test_play_audio_no_audio(mocker):
    """
    Test play_audio method when no audio is recorded.
    Assert that an exception is raised.
    """

    # arrange
    audio_processor = AudioProcessor()
    mocker.patch.object(audio_processor, 'recorded_audio', None)

    # act and assert
    with pytest.raises(Exception):
        audio_processor.play_audio()  # expect exception (None value)

def test_play_audio_with_audio(mocker):
    """
    Test play_audio method when audio is recorded.
    Assert that the audio is played.
    """

    # arrange
    # mock recorded audio data
    audio_processor = AudioProcessor()
    mock_audio_data = np.random.rand(48000, 1)
    mocker.patch.object(audio_processor, 'recorded_audio', mock_audio_data)
    # mock play method process
    mock_play = mocker.patch('sounddevice.play')
    mocker.patch('builtins.input', return_value="")
    mocker.patch('sounddevice.wait')

    # act
    audio_processor.play_audio()

    # assert
    assert mock_audio_data is not None, "Expected audio data"
    mock_play.assert_called_once_with(mock_audio_data, samplerate=48000)


def test_determine_dominant_pitch_in_hertz():
    """
    - test with predefined numpy array or series of attributes (numpy and non using fixtures)
    - calculate the dominant pitch in hertz
    - find frequency bins, and one with highest amplitude
    - returns correct

    How to test:
    - when no audio recorded, gracefully handled?
    - FTT calculation should match expected values from mock data

    """

    audio_processor = AudioProcessor()
    audio_processor.recorded_audio = None

    # act
    # TODO confirm doesn't stop other functions working - think of use case in broader scheme
    with pytest.raises(AttributeError):
        audio_processor.determine_dominant_pitch_in_hertz(), "No audio recorded yet. Please record audio first."

"""
Integration Testing:
Test the workflow of recording audio, determining dominant pitch,
and plotting the results (using mocks for hardware dependencies).
"""