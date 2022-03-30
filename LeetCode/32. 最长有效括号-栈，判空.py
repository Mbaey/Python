from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:

        
        stack = deque()
        m = [ 0 for i in range(len(s))]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack: # 如果是空的
                    # 标记多余的) 
                    m[i] = 1
                else:
                    stack.pop()
        # 多余的 (， 标记
        while stack: # 如果非空
            m[stack.pop()] = 1
        
        length = 0
        res = 0
        for i in m:
            if i == 1:
                length=0
            else:
                length += 1
            
            res = max(res, length)

        # res = 0


        return res
