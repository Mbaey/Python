from bisect import bisect_left
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_t = nums1[:m].copy()
        for i in range(n):
            idx = bisect_left(nums1_t, nums2[i])
            nums1_t.insert(idx, nums2[i])
            # print(idx)

        for j in range(m+n):
            nums1[j] = nums1_t[j]
        # nums1 = nums1_t
        # print(nums1)

if __name__ == "__main__":

    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(nums1,
                   3,
                   [2, 5, 6],
                   3)
    print(nums1)
