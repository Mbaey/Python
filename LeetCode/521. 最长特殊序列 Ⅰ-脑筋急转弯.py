from collections import Counter
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        if na < nb:
            return nb
        elif na > nb:
            return na
        else:
            if a == b:
                return -1
            if a != b:
                return na
            # res = 0
            # cnt1, cnt2 = Counter(a), Counter(b)
            # res1 = cnt1  - (cnt1 & cnt2)
            # res2 = cnt2  - (cnt1 & cnt2)
            # # sum([k*v for k,v in res1.items()]) 
            # return max( sum([v for k,v in res1.items()]),  sum([v for k,v in res1.items()])  )

        