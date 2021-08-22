import numpy as np
import matplotlib.pyplot as plt


def plot_spectrum(signal, fs):
    n = len(signal)
    d = 1 / fs

    hs = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, d)

    plt.plot(freqs, np.abs(hs))
    plt.xlabel("Frequence (Hz)")
    plt.ylabel("Amplitude")
    plt.title("spectrum，频谱")
    plt.show()
    return hs, freqs

## 时间, 信号,  窗口长度, 采样频率framerate


def make_spectrogram(times, signal, seg_length, fs):
    window = np.hamming(seg_length)
    i, j = 0, seg_length
    step = int(seg_length / 2)

    spec_map = {}

    while j < len(signal):
        segment = signal[i:j].copy()
        segment *= window

        t = (i+j) / 2

        hs = np.fft.rfft(segment)

        # 复数的模为信号的振幅（能量大小）
        spec_map[t] = hs

        i += step
        j += step

    freqs = np.fft.rfftfreq(seg_length, 1/fs)  # y_label
    steps = np.array(list(spec_map.keys()))  # x_label

    times_label = np.linspace(times[0], times[-1], len(steps))
    data_matrix = np.array(list(spec_map.values())).T  # data

    return data_matrix, times_label, freqs


def plot_spectrogram(times, signal, seg_length, fs, h=None, ax=None, title=None):
    d, x_label, y_label = make_spectrogram(times, signal, seg_length, fs)
    A = np.abs(d)


#     z_min = power.min().min()
#     z_max = power.max().max()
#     pc_kwargs = { 'cmap': 'Blues','vmin':z_min, 'vmax': z_max}
    pc_kwargs = {}

    if ax == None:
        ax = plt.axes()
    im = ax.pcolor(x_label, y_label, A, **pc_kwargs)

#     plt.colorbar(im)

    title = 'Spectrogram,时频谱' if not title else title
    ax.set(xlabel="Times (sec)", ylabel="Frequence (Hz)",
           title=title)

    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
    # ax.spines['bottom'].set_color('none')
    # ax.spines['left'].set_color('none')
    # ax.tick_params(direction='out', length=0, width=2, grid_alpha=0.5)

    if h:
        ax.set_ylim([0, h])

#    plt.savefig("spectrogram.svg",  bbox_inches='tight')
    ax.plot()
