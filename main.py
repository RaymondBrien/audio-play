import sounddevice as sd
import numpy as np
import queue
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Queue to send data from callback stream to main thread
q = queue.Queue()

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

def callback(indata, outdata, frames, time, status):  # TODO sort params
    """Callback function which receives live audio data"""
    if status:
        print(status)
    q.put(indata[:, 0])


def plot_pitch():
    """Plot the dominant pitch of the audio stream"""
    plt.ion()  # enable interactive mode
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot(x_data, y_data)

    while True:
        if not q.empty():
            audio_chunk = q.get()
            pitch = pitch_detection(audio_chunk, sample_rate=44100)
            if pitch:
                x_data.append(len(x_data))
                y_data.append(pitch)
                ax.clear()
                ax.plot(x_data, y_data, marker="o")
                ax.set_title("Dominant pitch over time:")
                ax.set_xlabel("Time")
                ax.set_ylabel("Frequency (Hz)")
                plt.pause(0.01)

stream = sd.InputStream(callback=callback, samplerate=44100, channels=2)
with stream:
    plot_pitch()