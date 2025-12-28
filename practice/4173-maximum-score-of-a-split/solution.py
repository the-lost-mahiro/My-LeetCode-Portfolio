class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefixSum = [0] * n
        
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        surfixMin = [float('inf')] * n
        surfixMin[-1] = nums[-1]
        for i in range(n - 2, 0, -1):
            surfixMin[i] = min(surfixMin[i + 1], nums[i])

        maxScore = float('-inf')
        for i in range(1, n):
            curScore = prefixSum[i] - surfixMin[i]
            maxScore = max(maxScore, curScore)

        return maxScore
