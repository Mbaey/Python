from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
import tensorflow.keras as keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def EnsemblePredict(models, X):
    length = X.shape[0]
    results = []
    for model in models:
        # len (0~nb_class)
        preds = model.predict(X)
        
        preds = preds.argmax(axis=1)
        results.append(preds)
    results = np.array(results)

    vote_preds=[]    
    for i in range(length):
        counts = np.bincount(results[:,i])
        vote_pred = np.argmax(counts)
        vote_preds.append(vote_pred)

    return np.array(vote_preds)

def Train(ModelClass, params, X, y, validation_data=None, batch_size=64, n_splits=5, one_fold=True, 
    epochs=200, verbose=0, log_fold_name="logs"):
    # 5-fold cross-validation
    kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    models = []

    for k, (train_index, test_index) in enumerate(kf.split(X, y)):
        X_train, y_train = X[train_index], y[train_index]
        X_dev, y_dev = X[test_index], y[test_index]

        #model = ModelClass(**params).to(device)
        model = ModelClass(**params)
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        filepath = f"Algorithm/eegnet-{k}.hdf5"#"-epoch{epoch:02d}-accuracy{accuracy:.2f}-val_accuracy{val_accuracy:.2f}.hdf5"
        # 中途训练效果提升, 则将文件保存, 每提升一次, 保存一次

        # checkpoint = ModelCheckpoint(filepath, monitor='val_accuracy', verbose=verbose, save_best_only=True, mode='max')
        print(f'fold{k} Training ------------')  # 开始训练
        print("Trian Data Size",X_train.shape)
        print("Dev Data Size",X_dev.shape)
        
        history = model.fit(X_train, y_train, batch_size=batch_size, validation_data=[X_dev, y_dev], 
                        epochs=epochs, verbose=verbose)#, callbacks=[checkpoint])
        df = pd.DataFrame(history.history)
        df.plot()
        print(df.describe())
       
        if one_fold:
            return model #, X_train, y_train, X_dev, y_dev 
        models.append(model)
    return models #, cvscores