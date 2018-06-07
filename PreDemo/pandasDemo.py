import pandas as pd
import numpy as np
# d = pd.Series([666, "fs", 21], index=['a', 'b', 'c'])
# if 'a'in d:
#     print(d.get('f', 1))
# print(d)

frame = pd.DataFrame(np.random.randint(low=1, high=10, size=(2,4)))
print(frame)
print(frame.describe())
