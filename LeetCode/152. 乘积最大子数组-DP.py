class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res=float("-inf")
        # imax, imin = float("-inf"), float("inf")
        res=nums[0]
        imax, imin = 1, 1
        for i in nums:
            if i < 0:
                imax, imin = imin, imax
            imax = max(imax*i, i)
            imin = min(imin*i, i)
            

            res = max(imax, res)
            
        return res