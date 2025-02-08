from matplotlib import pyplot as plt

def plot_pitch_graph():
    """Plot the dominant pitch of the audio stream"""
    plt.ion()  # enable interactive mode
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    line, = ax.plot(x_data, y_data)

    while True:
        if not q.empty():
            audio_chunk = q.get()
            pitch = pitch_detection(audio_chunk, sample_rate)
            if pitch:
                x_data.append(len(x_data))
                y_data.append(pitch)
                ax.clear()
                ax.plot(x_data, y_data, marker="o")
                ax.set_title("Dominant pitch over time:")
                ax.set_xlabel("Time")
                ax.set_ylabel("Frequency (Hz)")
                plt.pause(0.01)
