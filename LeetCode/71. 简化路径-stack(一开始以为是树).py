class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split("/")
        for dir in dirs:
            if dir == "":
                continue

            if stack == [] and dir == "..":
                continue
            
            if dir=="..":
                stack.pop(-1)
            
            elif dir==".":
                pass
            else:
                stack.append(dir)
        
        # print(stack)
        return "/"+"/".join(stack)
            
            
