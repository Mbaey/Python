import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        a,b=1,2
        res = 0
        for i in range(2, n):
            res = a + b
            a,b =b, res
        return res