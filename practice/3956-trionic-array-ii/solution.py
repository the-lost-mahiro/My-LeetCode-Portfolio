class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4: return 0

        dp0 = nums[0]
        dp1 = dp2 = dp3 = -float('inf')

        max_total = -float('inf')
        
        for i in range(1, n):
            curr = nums[i]
            prev = nums[i-1]

            p0, p1, p2, p3 = dp0, dp1, dp2, dp3

            dp0 = curr
            dp1 = dp2 = dp3 = -float('inf')
            
            if curr > prev:
                dp1 = max(p1 + curr, p0 + curr)
                dp3 = max(p3 + curr, p2 + curr)
                dp0 = max(curr, p0 + curr)
            elif curr < prev:
                dp2 = max(p2 + curr, p1 + curr)

            max_total = max(max_total, dp3)
            
        return max_total if max_total != -float('inf') else 0
