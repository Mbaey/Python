# from typing import List

import numpy as np

import re


class Solution:
    def isMatch(self, s: str, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        res = re.match(p, s)
        # print(res.group())
        if res == None:
            return False
        return res.group() == s


class Solution2():
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


if __name__ == "__main__":

    solution = Solution2()

    print(solution.isMatch("aa", "a."))
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("ab", ".*c"))
    # print( solution.isMatch(1212))
