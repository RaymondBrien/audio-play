import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from typing import Optional, ClassVar

# _________________________________________________________________
# default params
# run python3 -m sounddevice for available devices
sd.default.channels = 1 # input/output channels
default_sample_rate = sd.default.samplerate = 48000

TEST_DURATION = 1.0  # seconds
# _________________________________________________________________

# helper function to plot a stream of audio data
def pitch_detection(audio_data, sample_rate):
    """Find dominant frequency in audio data stream using FFT"""
    fft_spectrum = np.abs(np.fft.rfft(audio_data))
    freqs = np.fft.rfftfreq(len(audio_data), d=1/sample_rate)  # frequency bins
    peak_indices, _ = find_peaks(fft_spectrum, height=0.1)  # find peaks
    if len(peak_indices) > 0:
        dom_freq = freqs[peak_indices[np.argmax(fft_spectrum[peak_indices])]] # dominant frequency
        return dom_freq
    return None

class AudioProcessor:
    """
    AudioProcessor class to record audio from the user microphone and
    plot the FFT dominant frequency.

    Attributes:
    recording (bool): flag to indicate if audio is being recorded
    playing (bool): flag to indicate if audio is being played
    recorded_audio (np.array): recorded audio from the user microphone
    recording_duration (float): duration of the recording in seconds

    Flow:
    1. record audio
    2. play audio
    3. determine dominant pitch in hertz
    4. plot audio

    """

    def __init__(self) -> None:
        self.recording = False
        self.playing = False
        self.recorded_audio = None
        self.recording_duration = TEST_DURATION

    def __name__(self) -> str:
        return "AudioProcessor"


    def test_record(self) -> np.array:
        """Record audio from the user microphone"""

        self.recording = True
        print(f"Recording for {TEST_DURATION} seconds...")
        self.recorded_audio = sd.rec(int(TEST_DURATION * default_sample_rate))

        sd.wait()  # wait until recording is finished before continuing
        print("Done recording...")

        return self.recorded_audio


    def play_test_recording(self) -> np.array:
        """Play self.recorded_audio"""

        input("Press Enter to play the recorded audio...")

        print("Playing your recorded audio...")
        if self.recorded_audio is None:
            print("No audio recorded yet. Please record audio first.")
            return

        sd.play(self.recorded_audio, samplerate=default_sample_rate)
        sd.wait()


    def show_dom_pitch(self):
        """
        Plot dominant frequency of the recorded audio:

        - flatten recorded_audio (np.array)
        - calculate the dominant frequency using FFT
        """
        if self.recorded_audio is None:
            print("No audio recorded yet. Please record audio first.")
            pass

        # flatten audio array
        audio = self.recorded_audio.flatten()

        # calculate the dominant frequency using FFT
        dom_freq = np.fft.rfft(audio)

        # calculate frequency bins
        fft_freqs = np.fft.rfftfreq(len(self.audio), d=1/default_sample_rate)

        # find frequency with highest amplitude
        loudest_freq = self.fft_freqs[np.argmax(np.abs(dom_freq))]

        return dom_freq, fft_freqs, loudest_freq


    def plot_recorded_dom_pitch(self, dom_freq, fft_freqs, loudest_freq):
        """
        Plot the recorded audio

        Arguments:
        fft_freqs -- array of frequency bins
        dom_freq -- FFT result
        loudest_freq -- the loudest frequency in Hz
        """

        # plot result
        print(f"Dominantfrequency: {loudest_freq:.2f} Hz")
        plt.plot(fft_freqs, np.abs(dom_freq))
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Loudest Frequency was {:.2f} Hz".format(loudest_freq))
        plt.show()


