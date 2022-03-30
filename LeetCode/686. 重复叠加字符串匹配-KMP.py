class Solution:
    def strstr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pi[i] = j

        i, j = 0, 0
        while i - j < n:
            while j > 0 and haystack[i % n] != needle[j]:
                j = pi[j - 1]
            if haystack[i % n] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/repeated-string-match/solution/zhong-fu-die-jia-zi-fu-chuan-pi-pei-by-l-vnye/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。