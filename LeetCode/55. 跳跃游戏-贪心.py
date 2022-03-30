class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        a = 0
        b = nums[a]

        while a < n:
            # print(a,b)
            if a + b >= n-1:
                break
            maxi = 0
            max_ni = 0
            for i in range(a, a+b+1):
                if i + nums[i] > max_ni:
                    maxi = i
                    max_ni = i + nums[i]

            if a == maxi:
                break
            a = maxi
            b = nums[a]

        return a + b >= n -1
