from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(len(prices)-1):
            diff.append(prices[i+1] - prices[i])
        print(diff)
        res = 0
        pre = 0
        for i in diff:
            pre = pre + i

            res = max(res, pre)

            if pre < 0:
                pre = 0
        return res
