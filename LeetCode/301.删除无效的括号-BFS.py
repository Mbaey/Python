from typing import List

import numpy as np

#BFS: https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/cpython3java-1bfswu-xu-ji-he-by-hanxin_h-cwwe/
#回溯：https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/hui-su-suan-fa-jie-jue-qiong-ju-wen-ti-z-0e2m/
# https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/shan-chu-wu-xiao-de-gua-hao-by-leetcode-9w8au/
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type x: int
        :rtype: bool
        """
        def check(s: str) -> bool:
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        q = set()
        q.add(s)
        while True:
            ok_list = list(filter(check, q))
            if ok_list:
                return ok_list
            
            nxt_q = set()

            for x in q:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        nxt_q.add(x[ :i] + x[i + 1: ])                        
            q = nxt_q
        return list(q)

if __name__ == "__main__":

    solution = Solution()

    res = solution.removeInvalidParentheses('()())()')
    print(res)