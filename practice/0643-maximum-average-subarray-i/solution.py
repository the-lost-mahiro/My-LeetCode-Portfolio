class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k - 1
        total = 0

        for i in range(k):
            total += nums[i]

        max_total = total
        for _ in range(1, n - k + 1):
            total = total - nums[left] + nums[right + 1]

            if total > max_total:
                max_total = total

            left += 1
            right += 1
        
        return max_total / k
