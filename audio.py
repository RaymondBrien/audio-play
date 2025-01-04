import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# _________________________________________________________________
# default params
# run python3 -m sounddevice for available devices
sd.default.channels = 1 # input/output channels
default_sample_rate = sd.default.samplerate = 48000

TEST_DURATION = 1.0  # seconds
# _________________________________________________________________

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


    def record(self) -> np.array:
        """Record audio from the user microphone and plot the FFT dominant frequency"""

        # read the hertz from the user microphone
        print(f"Recording for {TEST_DURATION} seconds...")
        self.recorded_audio = sd.rec(int(TEST_DURATION * default_sample_rate))
        sd.wait()
        print("Done recording...")

        return self.recorded_audio


    def play_audio(self):
        """Play self.recorded_audio"""

        input("Press Enter to play the recorded audio...")

        print("Playing your recorded audio...")
        if self.recorded_audio is None:
            print("No audio recorded yet. Please record audio first.")
            return

        sd.play(self.recorded_audio, samplerate=default_sample_rate)
        sd.wait()


    def determine_dominant_pitch_in_hertz(self):
        """
        Plot dominant frequency of the recorded audio:

        - flatten self.recorded_audio (np.array)
        - calculate the dominant frequency using FFT
        - plot the recorded frequencies
        """

        # flatten audio array
        self.audio = self.recorded_audio.flatten()

        # calculate the dominant frequency using FFT
        self.dom_freq = np.fft.rfft(self.audio)

        # calculate frequency bins
        self.fft_freqs = np.fft.rfftfreq(len(self.audio), d=1/default_sample_rate)

        # find frequency with highest amplitude
        self.loudest_freq = self.fft_freqs[np.argmax(np.abs(self.dom_freq))]

        return self.loudest_freq


    def plot_audio(self):
        """Plot the recorded audio"""

        # plot result
        print(f"Dominantfrequency: {self.loudest_freq:.2f} Hz")
        plt.plot(self.fft_freqs, np.abs(self.dom_freq))
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.title("Loudest Frequency was {:.2f} Hz".format(self.loudest_freq))
        plt.show()


if __name__ == "__main__":

   audio = AudioProcessor()
   audio.record()
   audio.play_audio()