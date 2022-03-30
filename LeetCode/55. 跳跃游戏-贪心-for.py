class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_most = 0  # 记录最远能跳到哪
        for idx, val in enumerate(nums[:-1]): # 忽略最后一个位置
            right_most = max(right_most, idx+val)  # 当前位置上，最远能跳到哪
            # 如果最远都无法超过当前位置，那肯定无法到达最后一个位置，提前结束
            if right_most <= idx:
                return False 
        return True