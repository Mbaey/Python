import mne
import numpy as np
from datetime import datetime
import os
import keras.utils as ku

from moabb.datasets import gigadb
from .mne_utils import *


def get_Xy(sub=1):
    """
    funs:从raw里得到可监督学习的X，Y
    MI Interval：[0., 3.]
    All Interval：[-2., 5.]

    y:0->left, 1->right
    subs:s1 ~ ss52
    """
    datasets = gigadb.Cho2017()

    datamap = datasets.get_data([sub])
    raw = datamap[sub]["session_0"]["run_0"]
    raw_band = raw.copy()
    # Apply band-pass filter
    # ref: https://mne.tools/stable/auto_examples/decoding/plot_decoding_csp_eeg.html?highlight=montage
    raw_band.filter(8., 30.)

    X, y = get_Xy_fromRaw(raw_band, interval=[-1., 4.])
    FS = 512
    x_augmented, y_augmented = sliding_window(data=np.rollaxis(X, 2, 1),
                                              labels=y,
                                              window_sz=3 * FS,
                                              n_hop=FS // 4,
                                              n_start=0)

    y_augmented = ku.to_categorical(y_augmented-1)
    x_subject = x_augmented
    y_subject = y_augmented
    x_subject = np.rollaxis(x_subject, 2, 1)
    return x_subject, y_subject
