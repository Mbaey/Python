class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        b = nums[a]
        cnt = 0
        while a < n -1:
            # print(a,b)
            cnt += 1
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
            
        return cnt