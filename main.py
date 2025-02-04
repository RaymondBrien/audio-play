import sounddevice as sd
import argparse
import queue
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import find_peaks
from typing import Any, Callable

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-q', '--buffersize', type=int, default=20,
    help='number of blocks used for buffering (default: %(default)s)')
args = parser.parse_args()
print(f'Args: {args}')
if args.buffersize < 1:
    parser.error('buffersize must be at least 1')

# Queue to send data from callback stream to main thread
q = queue.Queue(maxsize=args.buffersize)

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

def callback(outdata, frames, time, status):  # TODO sort params
    """Callback function which receives live audio data"""
    assert frames

    assert not status
    if status:
        print(status)
    q.put(outdata[:, 0])
    try:

        data = q.get()
        print(f'Got data in queue: {data}')

    except queue.Empty or status.output_underflow:
        print('Output underflow: increase blocksize?')
        raise sd.CallbackAbort


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

stream = sd.InputStream(callback=callback, samplerate=44100, channels=1)
with stream:
    plot_pitch()
