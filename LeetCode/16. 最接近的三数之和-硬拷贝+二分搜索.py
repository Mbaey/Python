from bisect import bisect_left
from copy import deepcopy
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def find(nums, a, b):
            na = nums[a]
            nb = nums[b]
            nums.pop(a)
            nums.pop(b-1)

            idx = bisect_left(nums, target - na - nb)
            n = len(nums)

            # print(nums,a,b,idx, target - na - nb)

            if idx == n:
                return na + nb + nums[idx - 1]
            if idx == 0:
                return na + nb + nums[idx]
            l = na + nb + nums[idx - 1]
            r = na + nb + nums[idx]
            if abs(l-target) > abs(r-target):
                return r
            else:
                return l
            
            
        # diff = target / 3.
        # nums = [i - diff for i in nums]
        nums.sort()
        n = len(nums)
        res = 10000
        for i in range(n):
            for j in range(i+1, n):
                sum3 = find(deepcopy(nums), i, j)

                if abs(sum3-target) < abs(res-target):
                    res = sum3
                if res == target:
                    return res
            # break
        return res