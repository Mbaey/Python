from typing import List


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        length = len(a)
        length_b = len(b)
        res = 0

        multi = length_b // length
        aaa = a * multi
        if b in aaa:
            return multi
        elif b in aaa + a:
            return multi + 1
        elif b in aaa + a + a:
            return multi + 2
        return -1


if __name__ == "__main__":

    solution = Solution()
    # b = "abc"
    # print(b[1:0:1])
    # print(solution.repeatedStringMatch("abcd", "cdabcdab"))
    # print(solution.repeatedStringMatch("aa", "a"))
    print(solution.repeatedStringMatch("abc",
                                       "cabcabca"))

    # print(solution.repeatedStringMatch("abc", "abcb"))
    # print(solution.repeatedStringMatch("abc",
    #                                    "aabcbabcc"))
