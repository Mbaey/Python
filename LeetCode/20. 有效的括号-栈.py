class Solution:
    def isValid(self, s: str) -> bool:
        chars = "({[ ]})"
        char2id = { c: idx-3  for idx, c in enumerate(chars)}
        # print(char2id)
        
        stack = []
        
        for c in s:
            id = char2id[c]
            if id <0:
                stack.append(id)
            else:
                # n = len(stack)
                if stack and stack[-1] == -id:
                    del stack[-1]
                    # stack.pop()
                else:
                    return False
        
        return stack == []
