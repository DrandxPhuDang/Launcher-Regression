import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter


def spectrum_plot(Path_file_data, start_col, num_plots, object, list_object, target, path_save):
    global ax_spectrum
    read_data = pd.read_csv(fr'{Path_file_data}', sep=',')
    df = pd.DataFrame(read_data)
    list_features = df.iloc[:0, start_col:]
    get_features = [f'{e}' for e in list_features]
    list_spectrum = []
    for i_object in list_object:
        get_object = df[df[object] == f'{i_object}']
        list_spectrum.append(get_object)

    list_target = []
    for df_target in list_spectrum:
        get_target = df_target[target]
        list_target.append(get_target)

    def plot(ax_plot, data, features, color, title):
        data = data[features]
        data = savgol_filter(data, 11, polyorder=2, deriv=0)
        row, _ = data.shape  # so hang cua bo du lieu
        fmx = []
        for x in features:
            fmx.append(float(x))
        for i in range(0, row):
            ax_plot.plot(fmx, data[i], color=color)
        ax_plot.set_xticks(np.arange(int(min(fmx)), int(max(fmx)), 100))
        ax_plot.set_facecolor("white")
        ax_plot.set_title(title, fontweight='bold')
        ax_plot.grid()

    def plot_target(ax, data, title, color):
        ax.plot(data, color)
        ax.set_title(title, fontweight='bold')

    def plot_mean(data, label, start):
        y = data.values[:, start:]
        y = savgol_filter(y, 11, polyorder=2, deriv=0)
        y_mean = np.mean(y, axis=0)
        str_x = data.columns.values[start:]
        fmx = []
        for x in str_x:
            fmx.append(float(x))
        plt.plot(fmx, y_mean, label=label)
        ax_plot = plt.gca()
        ax_plot.set_xlabel(r'$\lambda$ (nm)', fontsize=15, fontweight='bold')
        ax_plot.set_ylabel('Spectra intensity', fontsize=15, fontweight='bold')

    fig, axes_spectrum = plt.subplots(nrows=num_plots, ncols=2)

    fig.suptitle('Spectrum ', fontsize=19, fontweight='bold')
    plt.subplots_adjust(left=0.076, right=0.96)
    try:
        for i, ax_spectrum in enumerate(axes_spectrum.flatten()):
            plot(ax_spectrum, list_spectrum[i], features=get_features, title=f'{list_object[i]}', color=None)
    except:
        pass
    fig.supxlabel(r'$\lambda$ (nm)', fontsize=15, fontweight='bold')
    fig.supylabel('Spectra intensity', fontsize=15, fontweight='bold')
    plt.savefig(path_save + r'\Spectrum' + '.png')

    # -----------------------------------------------------------------------
    plt.figure()
    plt.title('Mean Spectrum ', fontsize=19, fontweight='bold')
    try:
        for i, ax_spectrum in enumerate(axes_spectrum.flatten()):
            plot_mean(list_spectrum[i], start=start_col, label=f'{list_object[i]}')
    except:
        pass
    plt.legend()
    plt.grid(1)
    plt.savefig(path_save + r'\Mean Spectrum' + '.png')

    # -----------------------------------------------------------------------
    fig_target, axes_spectrum_target = plt.subplots(nrows=num_plots, ncols=2)
    try:
        for i_target, ax_spectrum_target in enumerate(axes_spectrum_target.flatten()):
            plot_target(ax_spectrum_target, list_target[i_target], title=f'{target} ' + f'({list_object[i_target]})',
                        color='Blue')
    except:
        pass
    fig_target.supxlabel('Sample number', fontsize=15, fontweight='bold')
    fig_target.supylabel(f'{target} Range', fontsize=15, fontweight='bold')
    plt.savefig(path_save + r'\Target' + '.png')

    plt.show()
    plt.close('all')
