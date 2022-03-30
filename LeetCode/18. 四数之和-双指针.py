class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def find(a, b):
            l,r=b+1, n-1
            
            while l<r:
                sum4 = nums[a] + nums[b] + nums[l] + nums[r]
                hashId = nums[a]*1e9 + nums[b]*1e6 + nums[l]
                
                if sum4 > target:
                    r -= 1
                elif sum4 < target:
                    l += 1
                else:
                    # 如果和等于 \textit{target}target，则将枚举到的四个数加到答案中，然后将左指针右移直到遇到不同的数，将右指针左移直到遇到不同的数；
                    # 不用Hash也可以去重。
                    if hashId not in s:
                        res.append([nums[a], nums[b] , nums[l] , nums[r]])
                        s.add(hashId)
                    l += 1

        res = []  
        s = set()      
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1, n-2):
                find(i, j)


        return res