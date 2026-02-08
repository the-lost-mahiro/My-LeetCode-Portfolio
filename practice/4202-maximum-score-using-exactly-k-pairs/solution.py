class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (k + 1) for _ in range(m + 1)]

        for j in range(m + 1):
            dp[j][0] = 0

        for i in range(1, n + 1):
            ndp = [[float('-inf')] * (k + 1) for _ in range(m + 1)]

            for j in range(m + 1):
                ndp[j][0] = 0

            for j in range(1, m + 1):
                for t in range(1, min(i, j, k) + 1):
                    ndp[j][t] = max(ndp[j][t], dp[j][t], ndp[j - 1][t])

                    if dp[j - 1][t - 1] != float('-inf'):
                        ndp[j][t] = max(ndp[j][t], dp[j - 1][t - 1] + nums1[i - 1] * nums2[j - 1])
            dp = ndp

        return dp[m][k]
