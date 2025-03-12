import pytest
import numpy as np
from unittest.mock import Mock

from src.sound.stream import AudioStream

@pytest.mark.parametrize(
    "test_id, samplerate, channels, blocksize",
    [
        ("happy_path_1", 44100, 1, 0),
        ("happy_path_2", 48000, 2, 1024),
        ("happy_path_3", 96000, 1, 2048),
        ("edge_case_1", 1, 1, 0),  # Minimum samplerate
        ("edge_case_2", 192000, 8, 4096), # Max values
        ("error_case_1", 0, 1, 0),  # Invalid samplerate
        ("error_case_2", 44100, 0, 0),  # Invalid channels
        ("error_case_3", 44100, 1, -1),  # Invalid blocksize
    ],
)
def test___init__(stdscr_mock, test_id, samplerate, channels, blocksize):
    # Arrange
    if "error_case" in test_id:
        expected_exception = ValueError
    else:
        expected_exception = None

    # Act
    if expected_exception:
        with pytest.raises(expected_exception):
            stream = AudioStream(stdscr=stdscr_mock, samplerate=samplerate, channels=channels, blocksize=blocksize)
    else:
        stream = AudioStream(stdscr=stdscr_mock, samplerate=samplerate, channels=channels, blocksize=blocksize)

        # Assert
        assert stream.samplerate == samplerate
        assert stream.channels == channels
        assert stream.blocksize == blocksize
        assert stream.stdscr == stdscr_mock


@pytest.fixture
def stdscr_mock():
    return Mock()

