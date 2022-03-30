import bisect
import collections
import math
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # print(math.comb(4, 2))
        # x=10
        # y<= 12
        # y > x
        # y>100 and x <100
        # print(ages)
        ages.sort()
        cnt = collections.Counter(ages)

        # print(ages)
        res = 0
        
        for i in range(len(ages)):
            x = ages[i]
            if x > 14 and cnt[x] > 1:
                res += math.comb(cnt[x], 2)  #cnt[x] - 1
                i += cnt[x]
                cnt[x] = 1
                # continue

        i = 0

        while i < len(ages):
            x = ages[i]
            bound = x *0.5 +7
            right = bisect.bisect_right(ages, bound)
            

            if right < i:
                res += i - right 
            
            i += 1

            # 2-2 3-6 4-12  组合.Cn_2 * 2
            # for j in range(i-1, right-1, -1):
            #     y = ages[j]
            #     # print(x, y, bound, res)
                
            #     # if y <=  bound:
            #     #     continue

            #     if x == y:
            #         res += 1
            #     else:
            #         break
            #     # else:
            #     #     res += 1 
            #         # break 
            #     # res += 1
        return res