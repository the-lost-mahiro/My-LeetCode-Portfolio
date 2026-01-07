class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        for i in range(1, n + 1):
            leftSum = prefixSum[i - 1]
            rightSum = prefixSum[-1] - leftSum - nums[i - 1]
            if leftSum == rightSum:
                return i - 1
        
        return -1
