class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final_total = float('-inf')
        current_total = float('-inf')
        for i in range(len(nums)):
            current_total = max(nums[i], current_total + nums[i])
            final_total = max(current_total, final_total)
        return final_total
