import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n < 3:
            return []

        
        nums.sort()
        cnt = collections.Counter(nums)
        num2idx = {i: idx for idx, i in enumerate(nums)}


        # for idx, i in enumerate(nums)
        # print(nums)
        s = set()
        for i in range(n):
            for j in range(i+1, n):
                numK = 0-nums[i]-nums[j]
                # print(nums[i], nums[j], numK)
                hashId = nums[i] * 1e5 + nums[j]
                if numK in cnt:
                    if hashId not in s and num2idx[numK]> j :
                        
                        s.add(hashId)
                        res.append([nums[i], nums[j], numK])

        return res