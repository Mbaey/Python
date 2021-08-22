import pickle
import os
from matplotlib import pyplot as plt 
import numpy as np
import mne
def load_data(path='../dataset/deap/data_preprocessed_python'):
    
    """"
    
    This function is responsible for loading the dataset from the disc.
    The path from which he dataset is obtained is constant.
    The function also assigns labels for each loaded sample.
    The labels are obtained on the basis of the valence and arousal values contained in the dataset.
    They are assigned according to the following rules:
        - 0 - Meditation:  Val > 5 Arousal < 5
        - 1 - Boredom:     Val < 5 Arousal < 5
        - 2 - Excitement:  Val > 5 Arousal > 5
        - 3 - Frustration: Val < 5 Arousal > 5
    In order to improve training results, 'strong' samples are being distinguished from the full set of data.
    Strong sample refers to one having both valence and arousal values close to the limits of the scale.
    For this case:
        Val / Arousal < 0.8 or Val / Arousal > 8.2
        
    ref：[CVaPR_EEG_videos/DataPreprocessing.py at 165c8533ecb9b2d1f8bd81e0193fec98cef7d898 · roosa123/CVaPR_EEG_videos](https://github.com/roosa123/CVaPR_EEG_videos/blob/165c8533ecb9b2d1f8bd81e0193fec98cef7d898/eeg_videos/DataPreprocessing.py)
    channels=["Fp1","AF3","F3","F7","FC5","FC1","C3","T7","CP5","CP1","P3","P7","PO3","O1","Oz","Pz","Fp2","AF4","Fz","F4","F8","FC6","FC2","Cz","C4","T8","CP6","CP2","P4","P8","PO4","O2"]
    """

    list_of_labels = []
    list_of_data = []
    files = []

    for (_, _, sets) in os.walk(path):
        files.extend(sets)

    files.sort()

    for file in files:
        #         print(file)
        participant_base = pickle.load(
            open(path + '/' + file, 'rb'), encoding='latin1')
        # ----------Labels - four discrete  states---------------

        labels = participant_base['labels']
        n, _ = labels.shape
        labels2 = np.zeros([n, 3])

        # States - labels IMPORTANT
        # 0 - Meditation  Val > 5 Arousal < 5 冥想
        # 1 - Boredom     Val < 5 Arousal < 5 无聊
        # 2 - Excitement  Val > 5 Arousal > 5 兴奋 
        # 3 - Frustration Val < 5 Arousal > 5 沮丧

        for i in range(n):
            labels2[i, 0] = i
            curr_valence = labels[i, 0]
            curr_arousal = labels[i, 1]
            if curr_valence > 5:
                if curr_arousal <= 5:
                    labels2[i, 1] = 0
                else:
                    labels2[i, 1] = 2
            else:
                if curr_arousal <= 5:
                    labels2[i, 1] = 1
                else:
                    labels2[i, 1] = 3

            if curr_valence > 7 or curr_valence < 3:
                if curr_arousal > 7 or curr_arousal < 3:
                    labels2[i, 2] = 1

        # -------------- Lists for labels and data------------------

        data = participant_base['data']
        list_of_labels.append(labels2)
        list_of_data.append(np.delete(data, np.s_[32:], axis=1)) # only choose egg channel
        # ----------------------------------------------------------

    print(len(list_of_labels))
    print(len(list_of_data), len(list_of_data[0]), len(list_of_data[0][0]))


    return list_of_labels, list_of_data, files
    
def get_Xy(path='../dataset/deap/data_preprocessed_python'):
    file = os.path.join(path, f"s-all.pkl")
    eeg_data = {}
    if not os.path.exists(file):
        list_of_labels, list_of_data, files = load_data(path)
        list_of_data = np.concatenate(list_of_data)
        list_of_label = np.concatenate(list_of_labels)
#         list_of_label = list_of_label[:,1:]
        eeg_data["x"] = list_of_data
        eeg_data["y"] = list_of_label
        with open(file, 'wb') as fw:
            pickle.dump(eeg_data, fw, protocol=4)
    else:
        with open(file, 'rb') as fr:
            eeg_data = pickle.load(fr)
    return eeg_data["x"],eeg_data["y"]