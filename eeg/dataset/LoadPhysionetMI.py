import mne
import numpy as np
from datetime import datetime
import os
# import keras.utils as ku

from moabb.datasets import physionet_mi
from .mne_utils import *

def get_Xy(sub=1):
    """
    funs:从raw里得到可监督学习的X，Y
    MI Interval：[0., 3.]
    All Interval：[-2., 5.]

    y:0->left, 1->right
    subs:s1 ~ ss52
    """
    physionetMI = physionet_mi.PhysionetMI()
    datamap = physionetMI.get_data(subjects=[sub])
    raw = mne.concatenate_raws([datamap[sub]["session_0"][_] for _ in datamap[sub]["session_0"]])
    
    raw_band = raw.copy()
    # Apply band-pass filter
    # ref: https://mne.tools/stable/auto_examples/decoding/plot_decoding_csp_eeg.html?highlight=montage
    raw_band.filter(8., 30.)


    X,y = get_Xy_fromRaw(raw_band, stim_channel="STI 014", event_id=dict(
            left_hand=2, right_hand=3, feet=5, hands=4), interval=[0, 3])    
	
    return X.astype("float32")[:,:,:-1], y.astype("int64")-2
	
def get_Xy_augmented(sub=1):
    """
    funs:从raw里得到可监督学习的X，Y
    MI Interval：[0., 3.]
    All Interval：[-2., 5.]

    y:0->left, 1->right
    subs:s1 ~ ss52
    """
    physionetMI = physionet_mi.PhysionetMI()
    datamap = physionetMI.get_data(subjects=[1])
    raw = mne.concatenate_raws([datamap[sub]["session_0"][_] for _ in datamap[sub]["session_0"]])
    
    raw_band = raw.copy()
    # Apply band-pass filter
    raw_band.filter(8., 30.)

    X,y = get_Xy_fromRaw(raw_band, stim_channel="STI 014", event_id=dict(
            left_hand=2, right_hand=3, feet=5, hands=4), interval=[-1., 4.])    
    
    return augment_train_data(X.astype("float32"),y.astype("int64")-2, FS=160)