from numpy.core.numeric import flatnonzero

from tensorboardX import SummaryWriter
import math
import datetime
import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

font = {'family' : 'SimHei',
        'weight' : 'bold',
        'size'   : '16'}
plt.rc('font', **font)               # 步骤一（设置字体的更多属性）
plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim.lr_scheduler as lr_scheduler

from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
from sklearn.metrics import roc_auc_score, precision_score, recall_score, accuracy_score, f1_score
from tqdm import tqdm

device = torch.device("cuda" if torch.cuda.is_available()
                      else "cpu")  # PyTorch v0.4.0
# device = torch.device("cpu")
torch.manual_seed(1)


def EnsemblePredict(models, X):
    length = X.shape[0]
    results = []
    for model in models:
        # len (0~nb_class)
        preds = Predict(model, X)

        results.append(preds)
    results = np.array(results)

    vote_preds = []
    for i in range(length):
        counts = np.bincount(results[:, i])
        vote_pred = np.argmax(counts)
        vote_preds.append(vote_pred)

    return np.array(vote_preds)


def Predict(model, X, device="cpu"):
    batch_size = 1
    res = []
    with torch.no_grad():
        model.eval()
        for i in range(0, len(X), batch_size):
            s, e = i, i + batch_size

            inputs = torch.from_numpy(X[s:e]).to(device)
            pred = model(inputs)
            res.append(pred.cpu().numpy().argmax(axis=1))

        model.train()
    return np.array(res).flatten()


def Predict_withProb(model, X, device="cpu"):
    """
    function的功能：使用nn模型，对输入数据X进行预测。

    Parameters
    ----------
    model:torch.nn
        模型
    X: ndarray, type=float32
        数据

    Return
    ----------
    preds：1d array, type=int64
        预测的标签
    max_prob：float
        置信度

    TODO：算Loss。2333
    """
    batch_size = 1

    flag = 0
    probs = None
    preds = None
    softmax = torch.nn.Softmax(dim=1)
    with torch.no_grad():
        model.eval()
        for i in range(0, len(X), batch_size):
            s, e = i, i + batch_size

            inputs = torch.from_numpy(X[s:e]).to(device)

            logits = model(inputs)

            prob = softmax(logits).cpu().numpy().max(axis=1)
            pred = logits.cpu().numpy().argmax(axis=1)

            if flag == 0:
                preds = pred
                probs = prob
                flag = 1
            else:
                preds = np.concatenate((preds, pred), axis=0)
                probs = np.concatenate((probs, prob), axis=0)

        model.train()
    return preds, probs


def Predict_withLoss(model, X, y, criterion=nn.CrossEntropyLoss()):
    """
    #ref: https://androidkt.com/calculate-total-loss-and-accuracy-at-every-epoch-and-plot-using-matplotlib-in-pytorch/
    function的功能：使用nn模型，对输入数据X进行预测。

    Parameters
    ----------
    model:torch.nn
        模型
    X: ndarray, type=float32
        数据

    Return
    ----------
    preds：1d array, type=int64
        预测的标签
    probs：1d array, type=float
        置信度
    loss: float
        损失    
    """

    batch_size = 32
    running_loss = 0
    total_num = math.ceil(len(X) / batch_size)

    flag = 0
    probs = None
    preds = None
    softmax = torch.nn.Softmax(dim=1)

    with torch.no_grad():
        model.eval()
        for i in range(0, len(X), batch_size):
            s, e = i, i + batch_size

            inputs = torch.from_numpy(X[s:e]).to(device)
            logits = model(inputs)

            y_batch = torch.from_numpy(y[s:e]).to(device)
            running_loss += criterion(logits, y_batch).item()

            prob = softmax(logits).cpu().numpy().max(axis=1)
            pred = logits.cpu().numpy().argmax(axis=1)

            if flag == 0:
                preds = pred
                probs = prob
                flag = 1
            else:
                preds = np.concatenate((preds, pred), axis=0)
                probs = np.concatenate((probs, prob), axis=0)

        model.train()
        test_loss = running_loss/total_num

    return preds, probs, test_loss


def Evaluate(model, X, Y, params=["acc"], criterion=nn.CrossEntropyLoss()):
    """
    function的功能：评估nn模型。

    Parameters
    ----------
    model:torch.nn
        模型
    X: ndarray, type=float32
        数据
    y: ndarray, type=int64
        标签
    params: str
        ["acc","auc", "recall","precision","fmeasure"]
    """
    results = []

    predicted, max_prob, test_loss = Predict_withLoss(
        model=model, X=X, y=Y, criterion=criterion)
    # print(type(predicted))
    # predicted = predicted.astype(float)
    for param in params:
        if param == 'acc':
            results.append(accuracy_score(Y, np.round(predicted)))
        if param == "auc":
            results.append(roc_auc_score(Y, predicted))
        if param == "recall":
            results.append(recall_score(Y, np.round(predicted)))
        if param == "precision":
            results.append(precision_score(Y, np.round(predicted)))
        if param == "fmeasure":
            precision = precision_score(Y, np.round(predicted))
            recall = recall_score(Y, np.round(predicted))
            results.append(2*precision*recall / (precision+recall))

    results.append(test_loss)
    return results


def Fit(model, X_train, y_train, validation_data, criterion=nn.CrossEntropyLoss(),
        epochs=100, batch_size=300, lr=0.001, verbose=0, log_n_hop=10, log_fold_name="logs"):
    """
    function的功能：nn模型拟合。

    Parameters
    ----------
    X_train: ndarray, type=float32
        训练数据
    y_train: ndarray, type=int64
        训练标签
    validation_data: list, ndarray
        测试用的数据与标签
    criterion: torch.nn.loss,
        loss Fun
        nn.CrossEntropyLoss() 、nn.MSELoss() ……
    verbose: int,
        if 0, no verbose
        if 1, print training log
        if 2, plot history and save to csv file
    log_n_hop：int,
        = epochs // log_nums
        e.g.:100 epochs, log 10 times, log_n_hop = 100 // 10 = 10
    ...

    Examples
    --------
    >>> fit(X_train, y_train, validation_data = [X_test,y_test], criterion=nn.CrossEntropyLoss())
    """
    history = pd.DataFrame()
    trn_acc = []
    trn_loss = []
    val_acc = []
    val_loss = []
    epoch_2_model = {}
    
    with SummaryWriter(comment=log_fold_name) as writer:
        optimizer = torch.optim.Adam(
            filter(lambda p: p.requires_grad, model.parameters()), lr=lr)

        scheduler = lr_scheduler.ExponentialLR(optimizer, gamma=0.95)
        # for epoch in tqdm(range(epochs)):
        for epoch in range(epochs):
            correct = 0
            total = 0
            train_size = X_train.shape[0]
            running_loss = 0
            total_num = math.ceil(train_size / batch_size)

            for i in range(0, train_size, batch_size):
                s, e = i, i + batch_size

                X_batch = torch.from_numpy(X_train[s:e]).to(device)
                y_batch = torch.from_numpy(y_train[s:e]).to(device)

                outputs = model(X_batch)

                loss = criterion(outputs, y_batch)
                # Backward and optimize
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

                # computy accuracy
                _, predicted = torch.max(outputs.data, 1)
                total += len(y_batch)
                correct += (predicted == y_batch).sum().item()

                running_loss += loss.item()
                niter = i // batch_size + epoch * (train_size // batch_size)
                writer.add_scalar('Train/Loss', loss.item(), niter)

            scheduler.step()  # 更新lr

            train_loss = running_loss / total_num
            correct_trn = correct / total # * 100
            writer.add_scalar('Train/EpochAcc', correct_trn, epoch)
            writer.add_scalar('Train/EpochLoss', train_loss, epoch)
            # print("lr", optimizer.state_dict()['param_groups'][0]['lr'])
            # 开始测试
            if validation_data:
                X_test, y_test = validation_data
                correct_val = Evaluate(model, X_test, y_test)
                writer.add_scalar('Test/EpochAcc', correct_val[0], epoch)
                writer.add_scalar('Test/EpochLoss', correct_val[-1], epoch)

            if verbose > 0:
                trn_acc.append(correct_trn)
                trn_loss.append(train_loss)
                if validation_data:
                    val_acc.append(correct_val[0])
                    val_loss.append(correct_val[-1])
            if epoch % log_n_hop == 0:
                epoch_2_model[epoch] = copy.deepcopy(model)

            if verbose > 0 and epoch % log_n_hop == 0:
                # vebose=1,just plot
                correct_trn = Evaluate(model, X=X_train.astype(
                    "float32"), Y=y_train, params=['acc'])
                log_str = f'epoch[{epoch}/{epochs}] ------ Train loss:%.4f, Train accuracy:%.2f%%. ' % (
                    correct_trn[-1], correct_trn[0])
                if validation_data:
                    log_str += "Dev loss:%.4f, Dev accuracy:%.2f.%%" % (
                        correct_val[-1], correct_val[0])
                print(log_str)

                if verbose > 1:
                    # plot sth
                    pass
                # log 日志

    history["trn_acc"] = trn_acc
    history["trn_loss"] = trn_loss
    if validation_data:
        history["val_acc"] = val_acc
        history["val_loss"] = val_loss

    if verbose > 0:
        now = datetime.datetime.now().strftime('%m{m}%d{d}-%H{h}%M{M}').format(y='年', m='月', d='日', h='时', M="分")
        
        history.plot(title=f"{log_fold_name}_{now}")

        history.to_csv(f"runs/{log_fold_name}_{now}.csv")

    return history, epoch_2_model


def Train(ModelClass, params, X, y, validation_data=None, criterion=nn.CrossEntropyLoss(),
          n_splits=5, one_fold=True, lr=0.001, epochs=90, batch_size=64, verbose=0, log_n_hop=10, log_fold_name="logs"):
    # 5-fold cross-validation
    kf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    cvscores = []
    models = []

    for k, (train_index, test_index) in enumerate(kf.split(X, y)):
        X_train, y_train = X[train_index], y[train_index]
        X_dev, y_dev = X[test_index], y[test_index]

        model = ModelClass(**params).to(device)

        print(f'fold{k} Training ------------')  # 开始训练
        print("Trian Data Size", X_train.shape)
        print("Dev Data Size", X_dev.shape)
        history, epoch_2_model = Fit(model, X_train, y_train, validation_data=[X_dev, y_dev],
            criterion=criterion, epochs=epochs, batch_size=batch_size,
            lr=lr, verbose=verbose, log_n_hop=log_n_hop, log_fold_name=log_fold_name)
        
        # 开始测试
        if validation_data:
            print('Evaluating model on test set...')
            X_test, y_test = validation_data
            # scores = Evaluate(model, X_test, y_test)[0]
            scores = Evaluate(model, X_test, y_test)
            print("Result on test set: %s: %.2f%%" % ("acc", scores[0] * 100))
            cvscores.append(scores[0] * 100)

        if one_fold:
            return epoch_2_model  # , X_train, y_train, X_dev, y_dev
        models.append(epoch_2_model)

        print("CV Result:%.2f%%" % np.mean(cvscores))
    return models  # , cvscores
