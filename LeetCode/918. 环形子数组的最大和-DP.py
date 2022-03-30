class Solution:


    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def getmax(new_l):
            res = new_l[0]
            pre = 0
            for i in new_l:
                res = max(pre+i, res)
                pre = pre + i
                if pre <= 0:
                    pre=0
            return res
        n = len(nums)

        min_idx = 0
        min_val = nums[0]
        min_sum = nums[0]
        pre = 0
        for i in range(n):

        
            val = nums[i]
            min_sum = min(min_sum, pre + val)
            pre = pre + val
            if pre >= 0:
                pre = 0
            
            if min_sum < min_val:
                min_val = min_sum
                min_idx = i

        new_l = []

        if min_idx < n-1:
            min_idx += 1
        new_l +=  nums[min_idx:] + nums[:min_idx] 
        # new_l += nums
        # print(min_idx, min_sum,  new_l)
        res1 = getmax(nums)
        res2 = getmax(new_l)

        return max(res1, res2)

# 想到了找出最小子数组和，然后把原数组组合。最大子数组就是连续的了。
# 根据108号测试样例，发现原始数组可能就是包含了最大子数组。
# https://leetcode-cn.com/problems/divide-two-integers/solution/shu-ju-jie-gou-he-suan-fa-san-chong-jie-igpwu/