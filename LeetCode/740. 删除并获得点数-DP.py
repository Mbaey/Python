class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ans = [0 for i in range(10001)]
        for i in nums:
            ans[i] += i

        ppre, pre = 0, ans[0]
        res1 = 0

        for i in range(1, 10001):
            res1 = max(pre, ppre+ans[i])
            ppre, pre = pre, res1
        return res1