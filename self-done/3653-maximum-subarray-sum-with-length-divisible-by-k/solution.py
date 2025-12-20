class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        final_total = float('-inf')
        length = len(nums)
        prefix = [0]*(length + 1)
        for i in range(length):
            prefix[i + 1] = prefix[i] + nums[i]

        for a in range(k):
            current_total = float('-inf')
            for i in range(a, length - length%k, k):
                if i + k <= length:
                    prefix_sum = prefix[i + k] - prefix[i]
                    current_total = max(prefix_sum, current_total + prefix_sum)
                    final_total = max(final_total, current_total)

        return final_total
