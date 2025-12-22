class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        
        dp = [1] * m
        
        for j in range(m):
            for k in range(j):
                if all(strs[i][k] <= strs[i][j] for i in range(n)):
                    dp[j] = max(dp[j], dp[k] + 1)
        
        return m - max(dp)
