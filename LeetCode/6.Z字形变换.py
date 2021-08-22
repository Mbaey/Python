from typing import List

import numpy as np


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        lengths = len(s)
        if numRows >= lengths or numRows== 1:
            return s
        
        if numRows <= 2:
            numCols = lengths//numRows
            numCols += 1  # 奇数
        else:
            numCols = lengths // (numRows*2-2)
            numCols = (numCols + 1) * (numRows-1)
        
        arr = np.zeros((numRows, numCols), dtype=str)
        i,j,k=0,0,0
        while k < lengths:
            while j < numRows and k < lengths:

                arr[j][i]=s[k]
                j += 1
                k += 1
            
            i += 1
            j -= 2
            while j > 0 and k < lengths:

                arr[j][i]=s[k]
                i += 1
                j -= 1
                k += 1
        
        # print(arr)
        for i in range(numRows):
            for j in range(numCols):
                if arr[i][j]:
                    res += arr[i][j]
        return res


if __name__ == "__main__":

    solution = Solution()

    res = solution.convert("PAYPALISHIRING", 3)
    print(res)

    # arr2 = np.zeros((4, 6), dtype=str)
    # print(arr2)
# PAHNAPLSIIGYIR
# PAHNAPLSIIGYIR
# PAYPALISHIRING

# PINALSIGYAHRPI
# PINALSIGYAHRPI
