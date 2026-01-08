class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        dp = [float('-inf')] * (n + 1)
        for i in range(1, m + 1):
            prev = dp[0]
            for j in range(1, n + 1):
                cur_val = nums2[i - 1] * nums1[j - 1]
                temp = dp[j]
                dp[j] = max(dp[j], dp[j - 1], prev + cur_val, cur_val)
                prev = temp

        return dp[-1]
