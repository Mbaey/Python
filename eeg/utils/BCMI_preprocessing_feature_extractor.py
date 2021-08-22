from typing import List, Tuple
import math as m
import os
import mne
from mne.preprocessing import ICA
import numpy as np
import scipy.signal as signal
from scipy.interpolate import griddata
from scipy.linalg import fractional_matrix_power
from sklearn.decomposition import FastICA
from sklearn.preprocessing import normalize, scale, MinMaxScaler
# import Algorithm.test1 as t1
# import scipy.sparse as sp


def butter_bandpass(low_cut, high_cut, fs, order=3):
    """
    :param low_cut: low frequency
    :param high_cut: high frequency
    :param fs: sampling rate of the signal
    :param order: order of the filter
    :return: numerator (b) and denominator (a) polynomials of the IIR filter
    """
    nyq = 0.5 * fs
    low = low_cut / nyq
    high = high_cut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a

# 带通滤波


def butter_bandpass_filter(data, lowcut=2, highcut=60, fs=250, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.filtfilt(b, a, data)  # 这个y的格式和data的格式一样
    return y

# ref https://stackoverflow.com/questions/12093594/how-to-implement-band-pass-butterworth-filter-with-scipy-signal-butter/12233959#12233959
# def butter_bandpass(low_cut, high_cut, fs, order=3):
#     """
#     :param low_cut: low frequency
#     :param high_cut: high frequency
#     :param fs: sampling rate of the signal
#     :param order: order of the filter
#     :return: numerator (b) and denominator (a) polynomials of the IIR filter
#     """
#     nyq = 0.5 * fs
#     low = low_cut / nyq
#     high = high_cut / nyq
#     sos = signal.butter(order, [low, high], btype='sos')
#     return sos

# # 带通滤波
# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
#     sos = butter_bandpass(lowcut, highcut, fs, order=order)
#     y = signal.sosfilt(sos, data)
#     return y


def notch(cutoff=50, Q=30, fs=256):
    """Initialize the notch filter.

    Args:
        cutoff (float): cut-off frequency. Default = 50.
        Q (float): Quality factor. Default = 30.
        fs (int): sampling frequency. Default = 256
    """
    cutoff = cutoff
    Q = Q

    nyq = 0.5 * fs
    w0 = cutoff / nyq
    b, a = signal.iirnotch(w0, Q)
    return b, a


def notch_filtfilt(data, catoff=50, Q=30, fs=200, axis=-1):
    """Apply the filter to data along a given axis.

    Args:
        data (array_like): data to filter
        axis (int): along which data to filter

    Returns:
        ndarray: Result of the same shape as data

    """
    b, a = notch(catoff, Q, fs)
    return signal.filtfilt(b, a, data, axis)


# ref: gumpy-signal
def artifact_removal(X, n_components=None, check_result=False):
    """Remove artifacts from data.

    The artifacts are detected via Independent Component Analysis (ICA) and
    subsequently removed. To plot the results, use
    :func:`artifact_removal`

    Args:
        X (array_like): Data to remove artifacts from
        n_components (int): Number of components for ICA. If None is passed, all will be used
        check_result (bool): Examine/test the ICA model by reverting the mixing.


    Returns:
        A 2-tuple containing

        - **ndarray**: The reconstructed signal without artifacts.
        - **ndarray**: The mixing matrix that wqas used by ICA.

    """

    ica = FastICA(n_components)
    S_reconst = ica.fit_transform(X.T)
    A_mixing = ica.mixing_
    if check_result:
        assert np.allclose(X, np.dot(S_reconst, A_mixing.T) + ica.mean_)

    return S_reconst.T, A_mixing


class EA_online_data:
    def __init__(self):
        self.n_trials = -1
        self.current_cov_matrix= None


def EA(raw_data: np.array, online_data: EA_online_data=None):
    """
    Function: process EEG Data By EA-（euclidean alignment，欧几里德空间对齐）
              EA算法，在欧氏空间中对齐**来自不同受试者**的脑电试验，使它们更加相似，从而提高新受试者的学习性能。

                ref:《IEEE Transactions on Biomedical Engineering2020
                    \He_Wu_2020_Transfer learning for Brain–Computer interfaces - A euclidean space data.pdf》


    :param raw_data: numpy array with the shape of (n_trials, n_channels, n_samples)
                online raw data is send one by one, which shape is (n_channels, n_samples)
                offline raw data's shape is (n_trials, n_channels, n_samples)
    """
    
    if online_data:
        # online raw data is send one by one, which shape is (n_channels, n_samples)
        n_channels, n_samples = raw_data.shape
        if online_data.n_trials == -1:
            online_data.current_cov_matrix =  np.zeros((n_channels, n_channels))
            online_data.n_trials = 0
        
        Xi = raw_data 
        online_data.current_cov_matrix +=  np.dot(Xi, Xi.T) / (Xi.shape[1] - 1)
        online_data.n_trials += 1

        Ri = online_data.current_cov_matrix / online_data.n_trials 
        Ri_hat = fractional_matrix_power(Ri, -0.5)
        # EA_EEG = np.zeros((n_channels, n_samples))
        EA_EEG = np.dot(Ri_hat, Xi)
        return EA_EEG

    else:
        #offline raw data's shape is (n_trials, n_channels, n_samples)
        n_trials, n_channels, n_samples = raw_data.shape
        Ri = np.zeros((n_channels, n_channels))
        EA_EEG = np.zeros((n_trials, n_channels, n_samples))
        for Xi in raw_data:
            Ri += np.dot(Xi, Xi.T) / (Xi.shape[1] - 1)
            # Ri += np.cov(Xi) # This is Too slow
        online_data = EA_online_data()
        online_data.current_cov_matrix = Ri
        online_data.n_trials = n_trials
        Ri /= n_trials

        Ri_hat = fractional_matrix_power(Ri, -0.5)

        for i, Xi in enumerate(raw_data):
            EA_EEG[i, :, :] = np.dot(Ri_hat, Xi)
            
        return EA_EEG, online_data


def preprocess_online(data: np.array, online_data: EA_online_data=None):
    """
    :param eeg_rawdata: numpy array with the shape of (n_channels, n_samples)
    :return: filtered EEG raw data
    """
    data = data[:, :]
    filtedData = notch_filtfilt(data, catoff=50, Q=35, fs=250)
    filtedData = butter_bandpass_filter(
        data, lowcut=2, highcut=60, fs=250, order=5)
    # starttime = datetime.datetime.now()
    # for i in range(7):
    res = EA(filtedData, online_data=online_data)
    
    # endtime = datetime.datetime.now()
    # print((endtime - starttime))
    return res


def preprocess_offline(data: np.array):
    """  
    :param eeg_rawdata: numpy array with the shape of (n_trials, n_channels, n_samples)
    :return: filtered EEG raw data

    Usage:
    X, EA_online_data = preprocess_offline(X)
    y = y
    """
    data = data[:, :, :]
    filtedData = notch_filtfilt(data, catoff=50, Q=35, fs=250)
    filtedData = butter_bandpass_filter(
        data, lowcut=2, highcut=60, fs=250, order=5)
    # starttime = datetime.datetime.now()
    filtedData = EA(filtedData[:, :, :])

    # endtime = datetime.datetime.now()
    # print((endtime - starttime))
    return filtedData
def preprocess_filter(data: np.array):
    """  
    :param eeg_rawdata: numpy array with the shape of (n_trials, n_channels, n_samples)
    :return: filtered EEG raw data

    Usage:
    X, EA_online_data = preprocess_offline(X)
    y = y
    """
    data = data[:, :, :]
    filtedData = notch_filtfilt(data, catoff=50, Q=35, fs=250)
    filtedData = butter_bandpass_filter(
        data, lowcut=2, highcut=60, fs=250, order=5)
    return filtedData

def preprocess_DE_PSD_image( X_train, do_normalize=True, ch_names= ['Fpz', 'Fp1', 'Fp2', 'AF3', 'AF4', 'AF7', 'AF8', 'Fz', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'FCz', 'FC1', 'FC2', 'FC3', 'FC4', 'FC5', 'FC6', 'FT7', 'FT8', 'Cz', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'T7', 'T8', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'TP7', 'TP8', 'Pz', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'POz', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'Oz', 'O1', 'O2']):


    locs_2d = ch_names_2_loc2d(ch_names)
    res = []
    for i in range(X_train.shape[0]):
        data = X_train[i]
        
        eeg_feature_de = compute_DE(data, sample_freq=250, window_size=0.4)
        eeg_feature_de= eeg_feature_de.reshape(1, -1)    

        eeg_feature_psd = extract_psd_feature(data, sample_freq=250, window_size=0.4)
        eeg_feature_psd = eeg_feature_psd.reshape(1, -1)
        
        if do_normalize:
            normalize(eeg_feature_de, axis=1)
            normalize(eeg_feature_psd, axis=1)

        eeg_feature = np.concatenate([eeg_feature_de, eeg_feature_psd], axis=1)
        eeg_image = gen_images(locs_2d, eeg_feature, n_gridpoints=20, normalize=do_normalize)    
        
        res.append(eeg_image)
        
    #     break
    X = np.concatenate(res, axis=0)
    return X

def preprocess(eeg_rawdata):
    """
    :param eeg_rawdata: numpy array with the shape of (n_channels, n_samples)
    :return: filtered EEG raw data
    """
    assert eeg_rawdata.shape[0] == 62
    eeg_rawdata = np.array(eeg_rawdata)
    temp = 0 - (eeg_rawdata.shape[1] % 5)
    if temp != 0:
        eeg_rawdata = eeg_rawdata[:, :temp]

    ch_names = ['FP1', 'FPZ', 'FP2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4',
                'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'CB1', 'O1', 'OZ', 'O2', 'CB2']
    info = mne.create_info(
        # 通道名
        ch_names=ch_names,
        # 通道类型
        ch_types=['eeg' for _ in range(62)],
        # 采样频率
        sfreq=1000
    )
    raw_data = mne.io.RawArray(eeg_rawdata, info)
    raw_data.load_data().filter(l_freq=1., h_freq=75)
    raw_data.resample(200)
    ica = ICA(n_components=5, random_state=97)
    ica.fit(raw_data)
    eog_indices, eog_scores = ica.find_bads_eog(raw_data, ch_name='FP1')
    a = abs(eog_scores).tolist()
    ica.exclude = [a.index(max(a))]
    ica.apply(raw_data)
    filted_eeg_rawdata = np.array(raw_data.get_data())

    return filted_eeg_rawdata

# ref: https://oneuro.cn/n/competitiondetail/607801357ad516303cc0d57e 2021-bci-competition-preliminary-framework-emotion-localverson.tar.gz


def extract_psd_feature(raw_data: np.array, sample_freq: int, window_size: int,
                        freq_bands: List[Tuple[int, int]] = [(1, 4), (4, 8), (8, 14), (14, 31), (31, 49)], stft_n=256):
    """
    :param raw_data: numpy array with the shape of (n_channels, n_samples)
    :param sample_freq: Sample frequency of the input
    :param window_size: Nums of seconds used to calculate the feature
    :param freq_bands: Frequency span of different bands with the sequence of
        [(Delta_start, Delta_end),
        (Theta_start, Theta_end),
        (Alpha_start, Alpha_end),
        (Beta_start, Beta_end),
        (Gamma_start, Gamma_end)]
    :param stft_n: the resolution of the stft
    :return: feature: numpy array with the shape of (n_feature, n_channels, n_freq_bands)
    """
    n_channels, n_samples = raw_data.shape

    point_per_window = int(sample_freq * window_size)
    window_num = int(n_samples // point_per_window)
    psd_feature = np.zeros((window_num, len(freq_bands), n_channels))

    for window_index in range(window_num):
        start_index, end_index = point_per_window * \
            window_index, point_per_window * (window_index + 1)
        window_data = raw_data[:, start_index:end_index]
        hdata = window_data * signal.hann(point_per_window)
        fft_data = np.fft.fft(hdata, n=stft_n)
        energy_graph = np.abs(fft_data[:, 0: int(stft_n / 2)])

        for band_index, band in enumerate(freq_bands):
            band_ave_psd = _get_average_psd(
                energy_graph, band, sample_freq, stft_n)
            psd_feature[window_index, band_index, :] = band_ave_psd
    return psd_feature.swapaxes(2, 1)


def _get_average_psd(energy_graph, freq_bands, sample_freq, stft_n=256):
    start_index = int(np.floor(freq_bands[0] / sample_freq * stft_n))
    end_index = int(np.floor(freq_bands[1] / sample_freq * stft_n))
    ave_psd = np.mean(energy_graph[:, start_index - 1:end_index] ** 2, axis=1)
    return ave_psd

# ref: https://github.com/aug08/4D-CRNN/blob/master/DEAP/DEAP_1D.py


def compute_DE(raw_data: np.array, sample_freq: int, window_size=1,
               freq_bands=[1, 4, 8, 13, 31, 75]):
    """
    :param raw_data: numpy array with the shape of (n_channels, n_samples)
    :param sample_freq: Sample frequency of the input
    :param window_size: Nums of seconds used to calculate the feature
    :param freq_bands: Frequency span of different bands with the sequence of
        [Delta_start, Theta_start,
        Alpha_start, Beta_start,
        Gamma_start, Gamma_end]
    :return: feature: numpy array with the shape of (n_feature, n_channels, n_freq_bands)
    """
    n_channels, n_samples = raw_data.shape

    point_per_window = int(sample_freq * window_size)
    window_num = int(n_samples // point_per_window)
    de_feature = np.zeros((window_num, n_channels, len(freq_bands)-1))
    total_de = []
    for window_index in range(window_num):
        start_index, end_index = point_per_window * \
            window_index, point_per_window * (window_index + 1)
        window_data = raw_data[:, start_index:end_index]

        # data = (data - data.mean()) / data.std()  # 正则化
        # fre_step = [1, 4, 8, 13, 31, 75]
        for band_index in range(len(freq_bands)-1):
            sub_fre = butter_bandpass_filter(
                window_data, freq_bands[band_index], freq_bands[band_index + 1], sample_freq, order=3)
            variance = np.var(sub_fre, axis=1, ddof=1)
            raw_de = np.log(2 * np.pi * np.e * variance) / 2
            # raw_de = (raw_de - raw_de.min())/(raw_de.max() - raw_de.min()) # 归一化
            de_feature[window_index, :, band_index] = raw_de

    return de_feature


def gen_matrix(features, n_gridpoints, normalize=True):
    x = [4, 5, 6, 3, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5,
         6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 7, 8, 3, 4, 5, 6, 7]
    y = [1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
         6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9]
    x = np.array(x)*2
    y = np.array(y)*2
    feat_array_temp = []

    n_colors = features.shape[2]
    #     n_colors = int(features.shape[1] / nElectrodes)

    for c in range(n_colors):
        feat_array_temp.append(features[:, :, c])

    n_samples = features.shape[0]
    temp_interp = []
    for c in range(n_colors):
        temp_interp.append(np.zeros([n_samples, n_gridpoints, n_gridpoints]))

    for i in range(n_samples):
        for c in range(n_colors):
            matrix = np.zeros((n_gridpoints, n_gridpoints))
            matrix[y, x] = [i for i in feat_array_temp[c][i, :]]
            # matrix = (matrix-matrix.min())/(matrix.max()-matrix.min())
            temp_interp[c][i, :, :] = matrix
        # if i % 1000 == 0:
        #     print('Interpolating {0}/{1}'.format(i + 1, n_samples))

    # Normalizing
    # for c in range(n_colors):
    #     if normalize:
    #         temp_interp[c][~np.isnan(temp_interp[c])] = \
    #             scale(temp_interp[c][~np.isnan(temp_interp[c])])
    #     temp_interp[c] = np.nan_to_num(temp_interp[c])

    return np.swapaxes(np.asarray(temp_interp), 0, 1)


def kalman_filter(data):
    batch, n_channels, n_features = data.shape
    lds_sbusqr_feature = []
    for i in range(n_features):
        channel_feature = []
        for j in range(n_channels):
            data_kalman = np.array(kalman(data[:, j, i]))

            std = data_kalman.std()

            if(std != 0):
                data_kalman = (data_kalman - data_kalman.mean()) / std
            else:
                data_kalman = np.zeros_like(data_kalman)
            channel_feature.append(data_kalman)
        channel_feature = np.array(channel_feature)
        # channel_feature = (channel_feature-channel_feature.mean())/channel_feature.std()
        lds_sbusqr_feature.append(channel_feature)

    lds_eeg_feature = np.array(lds_sbusqr_feature)
    # print('lds_eeg_feature', lds_eeg_feature.shape)
    eeg_feature = lds_eeg_feature.transpose(2, 1, 0)
    # print('eeg_feature', eeg_feature.shape)
    return eeg_feature


def kalman(data):
    # 这里是假设A=1，H=1的情况
    a = data
    # intial parameters
    n_iter = a.shape[0]
    sz = (n_iter,)  # size of array
    x = 0  # truth value (typo in example at top of p. 13 calls this z)
    # observations (normal about x, sigma=0.1)
    z = np.random.normal(x, 0.1, size=sz)

    z = a
    Q = 1e-5  # process variance

    # allocate space for arrays
    xhat = np.zeros(sz)  # a posteri estimate of x
    P = np.zeros(sz)  # a posteri error estimate
    xhatminus = np.zeros(sz)  # a priori estimate of x
    Pminus = np.zeros(sz)  # a priori error estimate
    K = np.zeros(sz)  # gain or blending factor

    R = 0.1 ** 2  # estimate of measurement variance, change to see effect

    # intial guesses
    xhat[0] = a[:5].mean()
    P[0] = 1.0

    for k in range(1, n_iter):
        # time update
        # X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
        xhatminus[k] = xhat[k - 1]
        Pminus[k] = P[k - 1] + Q  # P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1

        # measurement update
        # Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
        K[k] = Pminus[k] / (Pminus[k] + R)
        # X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
        xhat[k] = xhatminus[k] + K[k] * (z[k] - xhatminus[k])
        P[k] = (1 - K[k]) * Pminus[k]  # P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
    return xhat


# ref: https://github.com/DeepakRaya/Cognitive_classification_RNN_EEG_images/blob/2c295955471fd3c1cbe1585fbbbe6b8e0691b508/utils.py#L23

def cart2sph(x, y, z):
    x2_y2 = x**2 + y**2
    r = m.sqrt(x2_y2 + z**2)                    # r     tant^(-1)(y/x)
    elev = m.atan2(z, m.sqrt(x2_y2))            # Elevation
    az = m.atan2(y, x)                          # Azimuth
    return r, elev, az


def pol2cart(theta, rho):
    return rho * m.cos(theta), rho * m.sin(theta)


def azim_proj(pos):
    """
    Computes the Azimuthal Equidistant Projection of input point in 3D Cartesian Coordinates.
    """
    [r, elev, az] = cart2sph(pos[0], pos[1], pos[2])
    return pol2cart(az, m.pi / 2 - elev)


def ch_names_2_loc2d(ch_names=['Fpz', 'Fp1', 'Fp2', 'AF3', 'AF4', 'AF7', 'AF8', 'Fz', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'FCz', 'FC1', 'FC2', 'FC3', 'FC4', 'FC5', 'FC6', 'FT7', 'FT8', 'Cz', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'T7', 'T8', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'TP7', 'TP8', 'Pz', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'POz', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'Oz', 'O1', 'O2']
                     ):
    montage = mne.channels.make_standard_montage("standard_1020")
    pos = montage.get_positions()['ch_pos']

    locs_2d = []
    for i in ch_names:
        if i in pos:
            locs_2d.append(azim_proj(pos[i]))
    locs_2d = np.array(locs_2d)

    min_max_scaler = MinMaxScaler()
    min_max_scaler.fit(locs_2d)
    locs_2d = min_max_scaler.transform(locs_2d)
    return locs_2d


def gen_images(locs, features, n_gridpoints=32, normalize=True, edgeless=False):
    """
    Generates EEG images given electrode locations in 2D space and multiple feature values for each electrode
    :param locs: An array with shape [n_electrodes, 2] containing X, Y
                        coordinates for each electrode.
    :param features: Feature matrix as [n_samples, n_features]
                                Features are as columns.
                                Features corresponding to each frequency band are concatenated.
                                (alpha1, alpha2, ..., beta1, beta2,...)
    :param n_gridpoints: Number of pixels in the output images
    :param normalize:   Flag for whether to normalize each band over all samples
    :param edgeless:    If True generates edgeless images by adding artificial channels
                        at four corners of the image with value = 0 (default=False).
    :return:            Tensor of size [samples, colors, W, H] containing generated
                        images.

    :Usage:
   , ch_names= ['Fpz', 'Fp1', 'Fp2', 'AF3', 'AF4', 'AF7', 'AF8', 'Fz', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'FCz', 'FC1', 'FC2', 'FC3', 'FC4', 'FC5', 'FC6', 'FT7', 'FT8', 'Cz', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'T7', 'T8', 'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'TP7', 'TP8', 'Pz', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'POz', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8', 'Oz', 'O1', 'O2']
    montage = mne.channels.make_standard_montage("standard_1020")
    pos = montage.get_positions()['ch_pos']

    locs_2d = []
    for i in ch_names:
        if i in pos:
            locs_2d.append(azim_proj(pos[i]))
    locs_2d = np.array(locs_2d)

    # plt.scatter(locs_2d[:,0],locs_2d[:,1])
    fea = np.random.randint(size=(1,59*5), low=0,high=3)
    eeg_img = gen_images(locs_2d, fea, normalize=False)
    """
    feat_array_temp = []
    nElectrodes = locs.shape[0]     # Number of electrodes
    # Test whether the feature vector length is divisible by number of electrodes
    assert features.shape[1] % nElectrodes == 0
    n_colors = features.shape[1] // nElectrodes
    for c in range(n_colors):
        # features.shape为[samples, 3*nElectrodes]
        feat_array_temp.append(
            features[:, c * nElectrodes: nElectrodes * (c+1)])

    nSamples = features.shape[0]    # sample number 2670
    # Interpolate the values        # print(np.mgrid[-1:1:5j]) get [-1.  -0.5  0.   0.5  1. ]
    grid_x, grid_y = np.mgrid[
        min(locs[:, 0]):max(locs[:, 0]):n_gridpoints*1j,
        min(locs[:, 1]):max(locs[:, 1]):n_gridpoints*1j
    ]

    temp_interp = []
    for c in range(n_colors):
        temp_interp.append(np.zeros([nSamples, n_gridpoints, n_gridpoints]))

    # Generate edgeless images
    if edgeless:
        min_x, min_y = np.min(locs, axis=0)
        max_x, max_y = np.max(locs, axis=0)
        locs = np.append(locs, np.array(
            [[min_x, min_y], [min_x, max_y], [max_x, min_y], [max_x, max_y]]), axis=0)
        for c in range(n_colors):
            feat_array_temp[c] = np.append(
                feat_array_temp[c], np.zeros((nSamples, 4)), axis=1)

    # Interpolating
    for i in range(nSamples):
        for c in range(n_colors):
            temp_interp[c][i, :, :] = griddata(locs, feat_array_temp[c][i, :], (grid_x, grid_y),    # cubic
                                               method='cubic', fill_value=np.nan)

    # Normalizing
    for c in range(n_colors):
        if normalize:
            temp_interp[c][~np.isnan(temp_interp[c])] = \
                scale(temp_interp[c][~np.isnan(temp_interp[c])])

        temp_interp[c] = np.nan_to_num(temp_interp[c])

    # swap axes to have [samples, colors, W, H] # WH xy
    temp_interp = np.swapaxes(np.asarray(temp_interp), 0, 1)
    return temp_interp
