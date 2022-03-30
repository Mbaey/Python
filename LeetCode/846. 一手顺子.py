from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/hand-of-straights/solution/yi-shou-shun-zi-by-leetcode-solution-4lwn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 自己的代码，超时了。
# import bisect
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         res = False
#         n = len(hand)
#         groupN = n // groupSize
#         if n % groupSize != 0:
#             return False
#         hand.sort()
#         visit = [False for i in range(n)]
#         idx=0
#         for i in range(groupN):
#             val = hand[0]
#             del hand[0]
#             print(val, hand)

#             for j in range(1, groupSize):
#                 idx = bisect.bisect_left(hand, val+j)
#                 # print(idx)
#                 # print(idx, hand[idx], hand, val+j)

#                 if idx < len(hand) and hand[idx] == val +j:
#                     del hand[idx]
#                 else :
#                     return False

#         return True