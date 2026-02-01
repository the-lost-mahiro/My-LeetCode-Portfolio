class Solution:
    def finalElement(self, nums: List[int]) -> int:
        return max(nums[-1], nums[0])
