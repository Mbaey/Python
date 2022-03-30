class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        flag = []
        def dfs(idx):
            print(idx)
            if flag:
                
                return
            
            if idx >= n - 1:
                flag.append(True)

                return
        
            a = nums[idx]
            for i in range(a, 0, -1):
                dfs(idx+i)
                if flag:
                    return
                
        
        dfs(0)
        if flag:
            return True
        
        return False
