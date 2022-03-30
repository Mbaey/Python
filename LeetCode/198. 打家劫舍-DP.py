class Solution:
    def rob(self, nums: List[int]) -> int:
        # a:current
        # b:pre
        a,b=nums[0], 0
        # 
        res=a
        n = len(nums)

        for i in range(1, n):
            res = max(a, b+nums[i])
            a,b = res,a
            
            # print(a)
        return res