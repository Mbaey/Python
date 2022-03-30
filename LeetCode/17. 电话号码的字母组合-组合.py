class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        strs = []
        for c in digits:
            strs.append(phoneMap[c])
        
        res = []
        pre = []
        for stri in strs:
            if pre:
                m = len(pre)
                n = len(stri)
                # res *= n
                for i in range(m):
                    for j in range(n):
                        res.append( pre[i] +stri[j])
                pass
            else:
                for c in stri:
                    res.append(c)

            pre = res
            res = []
        return pre