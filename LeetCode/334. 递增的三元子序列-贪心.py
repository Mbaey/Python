class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        INF = 2**32
		# Python中可以用如下方式表示正负无穷：
		# float("inf"), float("-inf")
        min1 = INF + 1
        min2 = INF
        # print(min1, min2)
        # for i in range(n-2):
        #     if nums[i+1] > nums[i]:
        #         if nums[i+2] > nums[i+1]:
        #             return True
        for i in nums:
            if  min2 < i and INF > min2:
                print(min1, min2, i)
                return True

            if min1 > i:
                min1 = i
            if min1 < i and i < min2:
                min2 = i
            
            # print(min1, min2)
        

        return False