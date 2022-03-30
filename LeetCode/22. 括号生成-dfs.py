class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, depth):
            # depth: 左括号的数量
            # length - depth:右括号的数量
            
            length = len(s)
            l = depth
            r = length - l
            # print(s, depth)
            if length == 2 * n:
                res.append(s)
                return
            
            if l > r:
                if l < n:
                    dfs(s+"(", depth+1)

                dfs(s+")", depth)
            elif l == r:
                dfs(s+"(", depth+1)

        dfs("", 0)
        return res
