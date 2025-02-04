import pytest
import asyncio
import numpy as np

from ..src.sound.audio_processor import AudioProcessor

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

class Test_Audio_Processor_Class():
    @pytest.fixture(autouse=True)
    def setup_class(self):
        try:
            self.audio_processor = AudioProcessor()
            print("Audio Processor instantiated successfully\n")

            self.mock_recording = np.random.rand(48000, 1)  # 1s simulated audio data
            yield

            # add teardown code here if required TODO

        except Exception as e:
            print(e)


    def test_record_method(self, mocker):
        """Test record method of AudioProcessor class"""

        mocker.patch('sounddevice.rec', return_value=self.mock_recording)
        mocker.patch('sounddevice.wait')  # mock wait call

        # act
        result = self.audio_processor.record()

        # assert
        assert isinstance(result, np.ndarray), "Expected a NumPy array"
        # confirm data expected dimensions
        assert result.shape == self.mock_recording.shape, "Expected same shape as mock data"
        np.testing.assert_array_equal(result, self.mock_recording), "Expected same data in mock data and result data"

    def test_play_audio_no_audio(self, mocker):
        """
        Test play_audio method when no audio is recorded.
        Assert that an exception is raised.
        """

        # arrange
        mocker.patch.object(self.audio_processor, 'recorded_audio', None)

        # act and assert
        with pytest.raises(Exception):
            self.audio_processor.play_audio()  # expect exception (None value)


    def test_play_audio_with_audio(self, mocker):
        """
        Test play_audio method when audio is recorded.
        Assert that the audio is played.
        """

        # arrange
        mocker.patch.object(self.audio_processor, 'recorded_audio', self.mock_recording)
        # mock play method process
        mock_play = mocker.patch('sounddevice.play')
        mocker.patch('builtins.input', return_value="")
        mocker.patch('sounddevice.wait')

        # act
        self.audio_processor.play_audio()

        # assert
        assert self.mock_recording is not None, "Expected audio data"
        mock_play.assert_called_once_with(self.mock_recording, samplerate=48000)


    def test_determine_dominant_pitch_no_audio(self):
        """
        Test method when no audio recorded, gracefully handled.
        Assert that an exception is raised.
        """

        # act
        # TODO confirm doesn't stop other functions working - think of use case in broader scheme
        with pytest.raises(AttributeError):
            self.audio_processor.determine_dominant_pitch_in_hertz(
            ), "No audio recorded yet. Please record audio first."


    def test_determine_dominant_pitch__with_audio(self, mocker):
        """
        Test method with mock audio
        - calculate the dominant frequency using FFT
        - FTT calculation should match expected values from mock data
        """
        mocker.patch(
            self.audio_processor, 'recorded_audio', self.mock_recording).determine_doninant_pitch_in_hertz()

        # arrange


    def test_pitch_detection(self):
        """
        Test pitch detection method
        - assert that the method returns the expected pitch
        - check takes two params (audio, sample_rate) with correct type
        - check returns a float
        - check returns a value in the expected range
        """
        with pytest.raises(Exception):
            self.audio_processor.pitch_detection(
                self.mock_recording, 48000), "Expected two parameters"


    """
    Integration Testing:
    Test the workflow of recording audio, determining dominant pitch,
    and plotting the results (using mocks for hardware dependencies).
    """

# asyncio.run_coroutine_threadsafe()