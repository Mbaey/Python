import gumpy
import numpy as np
from datetime import datetime
import os
import keras.utils as ku

def load_preprocess_data(data, debug, lowcut, highcut, w0, Q, anti_drift, class_count, cutoff, axis, fs):
    """Load and preprocess data.

    The routine loads data with the use of gumpy's Dataset objects, and
    subsequently applies some post-processing filters to improve the data.
    """
    # TODO: improve documentation

    data_loaded = data.load()

    if debug:
        print('Band-pass filtering the data in frequency range from %.1f Hz to %.1f Hz... '
          %(lowcut, highcut))

        data_notch_filtered = gumpy.signal.notch(data_loaded.raw_data, cutoff, axis)
        data_hp_filtered = gumpy.signal.butter_highpass(data_notch_filtered, anti_drift, axis)
        data_bp_filtered = gumpy.signal.butter_bandpass(data_hp_filtered, lowcut, highcut, axis)

        # Split data into classes.
        # TODO: as soon as gumpy.utils.extract_trails2 is merged with the
        #       regular extract_trails, change here accordingly!
        class1_mat, class2_mat = gumpy.utils.extract_trials2(data_bp_filtered, data_loaded.trials,
                                                             data_loaded.labels, data_loaded.trial_total,
                                                             fs, nbClasses = 2)

        # concatenate data for training and create labels
        x_train = np.concatenate((class1_mat, class2_mat))
        labels_c1 = np.zeros((class1_mat.shape[0], ))
        labels_c2 = np.ones((class2_mat.shape[0], ))
        y_train = np.concatenate((labels_c1, labels_c2))

        # for categorical crossentropy
#         y_train = ku.to_categorical(y_train)

        print("Data loaded and processed successfully!")
        return x_train, y_train
def get_Xy(sub="B01"):
    DEBUG = True
    CLASS_COUNT = 2
    DROPOUT = 0.2   # dropout rate in float

    # parameters for filtering data
    FS = 250
    LOWCUT = 2
    HIGHCUT = 60
    ANTI_DRIFT = 0.5
    CUTOFF = 50.0 # freq to be removed from signal (Hz) for notch filter
    Q = 30.0  # quality factor for notch filter 
    W0 = CUTOFF/(FS/2)
    AXIS = 0

    #set random seed
    SEED = 42
    KFOLD = 5
    # ## Load raw data 
    # Before training and testing a model, we need some data. The following code shows how to load a dataset using ``gumpy``.
    # specify the location of the GrazB datasets
    data_dir = r'D:\li\=.=\eeg\hw\nn-STFT\dataset\BCICIV_2b_grazdata'

    subject = sub

    # initialize the data-structure, but do _not_ load the data yet
    grazb_data = gumpy.data.GrazB(data_dir, subject)

    # now that the dataset is setup, we can load the data. This will be handled from within the utils function, 
    # which will first load the data and subsequently filter it using a notch and a sbandpass filter.
    # the utility function will then return the training data. 取得每一次试验的所有数据，8s。
    x_train, y_train = load_preprocess_data(grazb_data, True, LOWCUT, HIGHCUT, W0, Q, ANTI_DRIFT, CLASS_COUNT, CUTOFF, AXIS, FS)


    # ## Augment data

    x_augmented, y_augmented = gumpy.signal.sliding_window(data = x_train[:,:,:],
                                                              labels = y_train[:],
                                                              window_sz = 4 * FS,
                                                              n_hop = FS // 5,
                                                              n_start = FS * 1)
    x_subject = x_augmented
    y_subject = y_augmented
    x_subject = np.rollaxis(x_subject, 2, 1)
    
    
    return x_subject,y_subject

import gumpy
import numpy as np
from datetime import datetime



import pickle
## emm 改名字啦， v2的y是一维的pytorch用 ， v1是keras用。
def get_Xy2(dataset_dir = "./dataset/BCICIV_2b_grazdata", sub="B01"): # _v2
    eeg_data = {}    
    
    file = os.path.join(dataset_dir, f"sub{sub}-win4-stride0.2 V2.pkl")

    if not os.path.exists(file):
        x_subject,y_subject=get_Xy(sub)
        eeg_data["x_subject"]=x_subject
        eeg_data["y_subject"]=y_subject
        with open(file, 'wb') as fw:
            pickle.dump(eeg_data, fw, protocol=4)
    else:
        with open(file, 'rb') as fr:
            eeg_data = pickle.load(fr)

    return eeg_data["x_subject"],eeg_data["y_subject"]
    
def get_Xy_v1(sub="B01"):
    eeg_data = {}
    dataset_dir = "./dataset/BCICIV_2b_grazdata"
    
    file = os.path.join(dataset_dir, f"sub{sub}-win4-stride0.2 V2.pkl")

    if not os.path.exists(file):
        x_subject,y_subject=get_Xy(sub)
        eeg_data["x_subject"]=x_subject
        eeg_data["y_subject"]=y_subject
        
        with open(file, 'wb') as fw:
            pickle.dump(eeg_data, fw, protocol=4)
    else:
        with open(file, 'rb') as fr:
            eeg_data = pickle.load(fr)
			
    return eeg_data["x_subject"], ku.to_categorical(eeg_data["y_subject"])

