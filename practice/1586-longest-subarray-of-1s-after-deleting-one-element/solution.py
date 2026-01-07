class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_length = 0
        deleted = 0

        while right < len(nums):
            if nums[right] == 0:
                deleted += 1

            while deleted > 1:
                if nums[left] == 0:
                    deleted -= 1
                left += 1
            
            right += 1
            max_length = max(max_length, right - left)

        return max_length - 1
