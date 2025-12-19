class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        left = 0
        n = len(nums)
        curSum = 0

        for right in range(n):
            curSum += nums[right]
            
            while curSum >= target:
                minLength = min(minLength, right - left + 1)
                curSum -= nums[left]
                left += 1

        return minLength if minLength != float('inf') else 0
