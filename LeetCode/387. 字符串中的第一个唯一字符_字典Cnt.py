import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_l=list(s)
        cnt = collections.Counter(s_l)
        
        for i, char in enumerate(s):
            if cnt[char] == 1:
                return i 

        return -1