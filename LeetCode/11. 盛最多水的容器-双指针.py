class Solution:
    def maxArea(self, height: List[int]) -> int:
		# ps：看了看提示。
        n = len(height)
        i,j = 0, n-1
        res = 0
        while i < j:
            hi, hj = height[i], height[j]
            res = max(res, min(hi, hj) * (j - i))
            if hi < hj:
                i += 1
            else:
                j -= 1
        
        return res
