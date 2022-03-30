import math
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <=2:
        #     return n
        
        a,b=n,0
        res = 0
        while a>=0:
            res += math.comb(a+b, a) #* math.comb(a+b, b)
            # print(a, b, res )
            a -= 2
            b += 1
        
        return res
