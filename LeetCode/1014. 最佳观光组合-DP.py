import copy
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        # a1 = copy.deepcopy(values) # 本来想，每次往后遍历一位，就把之前的全减1.后来发现记录之前的最大值即可。
        imax = values[0]
        pre_max = 0
        n  = len(values)
        for i in range(n):
            val = values[i]
            imax = max(imax, val+pre_max)
            pre_max = max(val, pre_max)
            pre_max -= 1

            # print(pre_max, imax)
        return imax
            

            
