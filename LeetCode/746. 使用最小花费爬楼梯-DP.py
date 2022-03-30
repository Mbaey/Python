class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a ,b = cost[0], cost[1]
        res = 0
        n = len(cost)
        for i in range(2, n):        
            res = min(a, b) + cost[i]
            a,b = b,res

        res = min(a, b)
        return res