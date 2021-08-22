from typing import List

import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = 0
        nums1 = np.array(nums1, dtype=np.int64)
        nums2 = np.array(nums2, dtype=np.int64)
        # nums1.
        nums = np.concatenate([nums1, nums2])
        nums.sort()
        l = len(nums)
        if l % 2:  # ==1， 奇数
            res = float(nums[l//2])
        else:
            res = float(nums[(l+1)//2] + nums[(l-1)//2])/2
        return res


if __name__ == "__main__":

    solution = Solution()

    res = solution.findMedianSortedArrays([1, 3], [2, 3])
    print(res)

    nums1 = np.array([1, 3])
    nums = np.concatenate([nums1, nums1])
    nums.sort()
    print(nums)
