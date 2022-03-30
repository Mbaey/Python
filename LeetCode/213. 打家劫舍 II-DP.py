class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        
        
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        # 计算 0~n-1
        ppre, pre = 0, nums[0]
        res1 = 0
        for i in range(1, n-1):
            res1 = max(pre, ppre+nums[i])
            ppre, pre = pre, res1
        # 计算 1~n
        ppre, pre = 0, nums[1]
        res2 = 0
        for i in range(2, n):
            res2 = max(pre, ppre+nums[i])
            ppre, pre = pre, res2

        return max(res1, res2)