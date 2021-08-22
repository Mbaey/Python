from typing import List

import numpy as np


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        max_len = 1
        length = len(s)
        for idx in range(length):
            half_len = 1
            while idx-half_len >= 0 and idx+half_len < length and s[idx-half_len] == s[idx+half_len]:

                if half_len*2+1 > max_len:
                    res = s[idx-half_len:idx+half_len+1]
                    max_len = half_len*2+1
            # 偶数
                half_len += 1
            
            half_len = 1
            while idx-half_len+1 >= 0 and idx+half_len < length and s[idx-half_len+1] == s[idx+half_len]:
                if half_len*2 > max_len:
                    res = s[idx-half_len+1:idx+half_len+1]
                    max_len = half_len*2
                half_len += 1
        return res


if __name__ == "__main__":

    solution = Solution()

    res = solution.longestPalindrome("cbbd")
    print(res)
