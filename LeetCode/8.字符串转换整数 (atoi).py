from typing import List

import numpy as np

class Solution:
    def myAtoi(self, s: str) -> int:
        # 1
        s = s.strip()
        # 2
        if not s:
            return 0

        isNega = 0
        if s[0] == "-":
            isNega = 1
            s = s[1:]
        elif s[0] == "+":
            isNega = 0
            s = s[1:]

        elif not s[0].isdigit() :
            return 0
        idx=0
        num_str = "0"
        
        while idx < len(s) and s[idx].isdigit():
            num_str += s[idx]
            idx += 1
        
        res = int(num_str)
        if isNega:
            res = -res
        
        if res > 2**31 - 1:
            res = 2**31 - 1
        if res < -2**31 :
            res = - 2**31 
        return res

if __name__ == "__main__":

    solution = Solution()
    # if not "":
    #     print("ssss")
    # int("+++sdsd")
    res = solution.myAtoi("+1")

    print(res)


    # s = "a222"
    # print(s[0].isnumeric())
    print(2**31 )
