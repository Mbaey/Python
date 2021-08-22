from typing import List
# a = [1,2]
# print(len(a))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+ nums[j] == target:
                    return [i,j]

# [小白 Python 几种解法 - 两数之和 - 力扣（LeetCode）](https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/)
# 我服了。。搞得这么复杂。。不过后面几种方法有点价值