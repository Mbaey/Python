from typing import List

import numpy as np

# [Python学习中的“按位取反”笔记总结 - 逝水经年 - 博客园](https://www.cnblogs.com/jniantic/p/12189648.html)
class Solution:
    def reverse(self, x: int) -> int:

        res = str(x)
        flag = 0
        if x < 0:
            res = res[1:]
            flag = 1
        res = res[::-1]

        if flag:
            res = "-" + res
        res = int(res)

        if res > 2**31 - 1 or res < - (2**31):
            res = 0
        return res


if __name__ == "__main__":

    solution = Solution()

    res = solution.reverse(-123)
    print(res)

    print(2**31 )
