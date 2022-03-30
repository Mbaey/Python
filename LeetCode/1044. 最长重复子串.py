from bisect import bisect_left
from typing import List
import collections


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)

        set_len = len(set(s))
        if set_len == length:
            return ""
        if set_len == 1:
            return s[:-1]

        char_cnt = collections.defaultdict(int)
        char_2_idxs = collections.defaultdict(list)
        for idx, c in enumerate(s):
            char_cnt[c] += 1
            char_2_idxs[c].append(idx)
            # if c not in char_2_first_idx:
            #     char_2_first_idx[c] = idx

        max_len = 0
        res_str = ""
        for char, idxs in char_2_idxs.items():
            if char_cnt[char] == 1:
                continue

            for idx in idxs:

                for i in range(max_len+1, length):
                    substr = s[idx:idx+i]

                    old_idx = idx + 1
                    new_idx = s.find(substr, old_idx)

                    if new_idx != -1:
                        max_len = i
                        res_str = substr
                    else:
                        break
    

        # print(char_cnt)

        return res_str


        # for char in
if __name__ == "__main__":

    # s = 'mississippi'
    # d = collections.defaultdict(int)
    # for k in s:
    #     d[k] += 1
    # print(d)
    # print(d["a"])

    solution = Solution()
    # nums1 = [1, 2, 3, 0, 0, 0]
    # print(solution.longestDupSubstring("abcabc"))
    print(solution.longestDupSubstring("aaaa"))
    print(solution.longestDupSubstring("banana"))

    # print(ord('a') )
    # print(ord('z') )
