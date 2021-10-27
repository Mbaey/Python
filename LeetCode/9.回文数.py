from typing import List

import numpy as np

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        x_len = len(x_str)
        flag = True
        for i in range(x_len//2):
            if x_str[i] != x_str[x_len-i-1]:
                return False
        # if x_len % 2 == 1: # 0,1,2
        # else: 
        #     for i in range(x_len):
        #         if x_str[i] != x_str[x_len-i]:
        #             return False
        return True


if __name__ == "__main__":

    solution = Solution()

    res = solution.isPalindrome(-123)
    print(res)

    print( solution.isPalindrome(121))
    print( solution.isPalindrome(1212))
