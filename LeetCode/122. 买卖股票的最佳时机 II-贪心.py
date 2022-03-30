class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(len(prices)-1):
            diff.append(prices[i+1] - prices[i])
        
        res = 0
        pre = 0
        for i in diff:
            
            if i > 0:
                res += i
            # res = max(res, pre + i)
            # if res > pre:

            # pre = pre + i
            # if pre < 0:
            #     pre = 0
            
        return res