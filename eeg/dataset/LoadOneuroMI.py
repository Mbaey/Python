import mne
import pickle
import numpy as np
import sys
import os
# from utils.mne_utils import *

sys.path.append('.')
sys.path.append('utils')
from mne_utils import *
import re
import glob
def get_data(data_dir = r'C:\Users\li\Downloads\Compressed\MI_all'):
    
    # paths = glob.glob(os.path.join(data_dir, f"*/*.pkl"))
    paths = glob.glob(os.path.join(data_dir, f"*/*/*.pkl"))
    # paths.append()
    print(paths)
    def to_event(x):   
        if x not in [201,202,203]:
            return 0
        else:
            return x

    X_all=None
    y_all=None
    person_all=None
    flag=True
    for file in paths:
        
        path = file
        
        with open(file, 'rb') as fr:
            data = pickle.load(fr)

        label = data['data'][-1,:]
        eeg_data = data['data'][:-1,:]

        ch_names = data['ch_names'] +['stim']
        ch_types = ['eeg'] * 64 + ['stim']

        info = mne.create_info(ch_names=ch_names, ch_types=ch_types,
                                sfreq=250)

        label = list(map(to_event, label))
        label = np.array(label)[None,:]

        raw = mne.io.RawArray(data=np.vstack([eeg_data, label]), info=info, verbose=False)

        X,y=get_Xy_fromRaw(raw=raw, interval=[-0.004, 6.996],  stim_channel="stim", event_id=None, verbose=False)
    #     print(y.size == 3)
    #     print("###################")
        y -= 201
        

        person_id = re.findall(r"S0(\d)",path)[0]
        factor = 0 if "A" in path else 5
        person_ids = np.ones_like(y)*(int(person_id) + factor)
        print(file)
        print(person_ids)

        if flag:
            
            X_all = X
            y_all = y
            person_all = person_ids
            flag=False
        else:
            X_all = np.concatenate([X_all,X])
            y_all = np.concatenate([y_all,y])
            person_all = np.concatenate([person_all,person_ids])       
    #     break
    return X_all, y_all, person_all

if __name__ == '__main__':
#     starttime = datetime.datetime.now()
    #long running

	X_all, y_all, person_all = get_data()
	with open('TrainDataAll-mne.pkl', 'wb') as fw:
		pickle.dump({"X":X_all,"y":y_all,"person_all":person_all}, fw,protocol=4) 
	
"""
# Usage:

import pickle
import numpy as np
from scipy import signal
with open('TrainDataAll-mne.pkl', 'rb') as fr:
    data = pickle.load(fr)
    X_all=data['X']
    y_all=data['y']    
    person_all = data['person_all']

"""