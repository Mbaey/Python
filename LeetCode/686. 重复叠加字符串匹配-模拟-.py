from typing import List


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        length = len(a)
        length_b = len(b)
        res = 0

        b = b.replace(a, "")
        res += (length_b - len(b)) // length
        # print(b)
        # print(res)
        if b == "":
            return res

        if len(b) == length:
            pass
            b2 = b + b
            # print(b2)
            for i in range(length):
                new_b = b2[i:i+length]
                if new_b == a:
                    return res + 2

            return -1
        elif len(b) < length:
            a2 = a + a
            length_b = len(b)
            for i in range(length_b):
                b_s = b[:i]
                b_end = b[i:]
                res_s = 0 if len(b_s) == 0 else 1
                res_end = 0 if len(b_end) == 0 else 1
                if a.startswith(b_s) and b_end == "":
                    return res + 1
                if a.endswith(b_end) and b_s == "":
                    return res + 1
                if a.startswith(b_end) and a.endswith(b_s):
                    return res + res_end + res_s

            return -1
        else:
            return -1

        # while True:
        #     l = b.find(a)
        #     if l == -1:
        #         break


if __name__ == "__main__":

    solution = Solution()
    # b = "abc"
    # print(b[1:0:1])
    # print(solution.repeatedStringMatch("abcd", "cdabcdab"))
    # print(solution.repeatedStringMatch("aa", "a"))
    # print(solution.repeatedStringMatch("abc",
    #                                    "abcabca"))
    # print(solution.repeatedStringMatch("abc", "abcb"))
    print(solution.repeatedStringMatch("abc",
                                       "aabcbabcc"))
