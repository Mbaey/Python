class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow,fast = 0,0
        n = len(nums)
        while fast<n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            
            fast += 1
        return slow