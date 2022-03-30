class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # for i in range(n):

        #     for j in range(i+1, i+k+1):
        #         if j < n:
        #             if nums[i] == nums[j]:
        #                 return True
        # return False
        s = set()

        for i in range(k+1):
            if i < n:
                if nums[i] not in s:
                    s.add(nums[i])
                else:
                    return True
        
        for i in range(k+1, n):
            # print(i, i-k-1)
            s.remove(nums[i-k-1])
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        return False

            
                