import mne
import numpy as np
from datetime import datetime
import os

from sklearn.model_selection import StratifiedKFold, train_test_split


def get_Epoch(raw, interval=[-2.0, 5.0], stim_channel="Stim",
              event_id={"left_hand": 1, "right_hand": 2}, verbose=True):
    """
    funs:从raw里得到可监督学习的X，Y
    """
    events = mne.find_events(raw, stim_channel=stim_channel, verbose=verbose)

    picks = mne.pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False,
                           exclude='bads')

    epochs = mne.Epochs(raw, events, event_id=event_id, picks=picks,
                        tmin=interval[0], tmax=interval[1], baseline=None, proj=False, preload=True, verbose=verbose)

#     epochs.plot()
#     fig = mne.viz.plot_events(events, event_id=event_id, sfreq=raw.info['sfreq'],
#                               first_samp=raw.first_samp)
    return epochs


def get_Xy_fromRaw(raw, interval=[-2.0, 5.0], stim_channel="Stim",
                   event_id={"left hand": 1, "right hand": 2}, verbose=True):
    """
    funs:从raw里得到可监督学习的X，Y
    MI Interval：[0., 3.]
    All Interval：[-2., 5.]

    """
    epochs = get_Epoch(raw, interval, stim_channel, event_id, verbose=verbose)
    X = epochs.get_data()

    y = epochs.events[:, -1]
#     y = ku.to_categorical(y-1)
    return X, y


def sliding_window(data, labels, window_sz, n_hop, n_start=0, n_end=-1, show_status=False):
    """

    input: (array) data : matrix to be processed

           (int)   window_sz : nb of samples to be used in the window

           (int)   n_hop : size of jump between windows           

    output:(array) new_data : output matrix of size (None, window_sz, feature_dim)



    """
    if n_end == -1:
        n_end = data.shape[1]

    flag = 0

    for sample in range(data.shape[0]):

        tmp = np.array([data[sample, i:i + window_sz, :]
                        for i in np.arange(n_start, n_end - window_sz, n_hop)])

        tmp_lab = np.array([labels[sample] for i in np.arange(
            n_start, n_end - window_sz, n_hop)])

        if sample % 100 == 0 and show_status == True:

            print("Sample " + str(sample) + "processed!\n")

        if flag == 0:

            new_data = tmp

            new_lab = tmp_lab

            flag = 1

        else:

            new_data = np.concatenate((new_data, tmp))

            new_lab = np.concatenate((new_lab, tmp_lab))

    return new_data, new_lab


def augment_data(X, y, FS=160, ts=3, n_hop=0.1, n_start=0, n_end=-1):
    x_augmented, y_augmented = sliding_window(data=np.rollaxis(X, 2, 1),
                                              labels=y,
                                              window_sz=int(FS * ts),
                                              n_hop=int(FS * n_hop),
                                              n_start=n_start,
                                              n_end=n_end)
    x_augmented = np.rollaxis(x_augmented, 2, 1)
    return x_augmented, y_augmented


def augment_train_data(X, y, FS=160, test_size=0.2, ts=3, n_hop=0.1, n_start=0, n_end=-1):
    """
    test_size : 只对训练集进行数据增强
    """
#     print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=2020)

    x_augmented, y_augmented = augment_data(X_train, y_train, FS=FS, ts=ts,
                                            n_hop=n_hop, n_start=n_start, n_end=n_end)

    print("x_augmented.shape", x_augmented.shape)
    print("X_train", X_train.shape)
    return x_augmented, y_augmented, X_test, y_test
