import pandas as pd
import numpy as np
import scipy
from sklearn import preprocessing,model_selection,linear_model


def Mychisquare(*data):
    y_test, y_pre = data
    chisq, p = scipy.stats.chisquare(y_test, y_pre)
    print(chisq, p)
#     print("chisq----> %d,p值----> %d"%(chisq,p))

def LogisticRegression_multinomial(*data):
    X_train, X_test, y_train, y_test = data
    regr = linear_model.LogisticRegression()
    regr.fit(X_train, y_train)
    y_pre = regr.predict(X_test)
    Mychisquare(y_test, y_pre)
    print('Score: %.4f' % regr.score(X_test, y_test))
    print('Coefficients:%s, intercept %s' % (regr.coef_, regr.intercept_))
    showCoef(regr.coef_)

def showCoef(listCoef):
    print("下面是各项指标的权重")
    for i in range(len(listCoef[0])):
        print("    ", i, " ", queryData.columns[i], " : ", listCoef[0][i])
    print("\nREFCV属性筛选---->all")
    f = listCoef[0][3] * 31.7
    print("\n以公共财政收入同比增长为标准,兰州市对人才的吸引力增加了百分之 %.3f" % f)

ppd_list = 'finalDataCountry.csv'
queryData = pd.read_csv(ppd_list)
print(queryData.columns)
X_train = np.array(queryData.drop(["score"], axis=1).values)
y_train = np.array(queryData["score"].values)
X_train = preprocessing.scale(X_train)
cv_split = model_selection.ShuffleSplit(n_splits=10, test_size=.3, train_size=.7,random_state=0)
cv_results = model_selection.cross_validate(linear_model.LogisticRegressionCV(), X_train, y_train, cv=cv_split)

print(cv_results['train_score'].mean())
print(cv_results['test_score'].mean())
LogisticRegression_multinomial(X_train,X_train,y_train,y_train)