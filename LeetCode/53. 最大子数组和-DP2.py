from typing import List
import numpy as np


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        pre = 0
        for i in nums:
            pre = max(pre + i, i)
            res = max(pre, res)
            # if pre <= 0:
            #     pre=0
            # res = max(res, )
            # print(pre, res)
        return res
