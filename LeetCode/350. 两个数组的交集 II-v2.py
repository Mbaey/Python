import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1 
        
        nums1_cnt = collections.defaultdict(int)
        nums2_cnt = collections.defaultdict(int)
        for idx, c in enumerate(nums1):
            nums1_cnt[c] += 1
            
        for idx, c in enumerate(nums2):
            nums2_cnt[c] += 1

        res_l = []

        for k, v in nums2_cnt.items():
            if k in nums1_cnt:
                res_l += [k] * min(nums1_cnt[k], nums2_cnt[k])

        return res_l
    
