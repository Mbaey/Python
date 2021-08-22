
import pandas as pd

df = pd.read_excel("第四轮 学科评估 - 软件工程.xlsx")

# df.head()

df.fillna(method="ffill", inplace=True)

df["学校代码及名称"] = df["学校代码及名称"].str.replace("\xa0\xa0\xa0\xa0\xa0\xa0", " - ")

school_Score_maps = {df.iloc[i, 1]: df.iloc[i, 0] for i in range(df.shape[0])}

print(school_Score_maps)
