class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[[0 for _ in range(k)] for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    remainder = grid[i][j] % k
                    dp[i][j][remainder] += 1
                for r in range(k):
                    if i == 0 and j == 0:
                        pass
                    else:
                        remainder = (r + grid[i][j])%k
                        if i == 0:
                            dp[i][j][remainder] += dp[i][j-1][r]
                        elif j == 0:
                            dp[i][j][remainder] += dp[i-1][j][r]
                        else:
                            dp[i][j][remainder] += dp[i-1][j][r]
                            dp[i][j][remainder] += dp[i][j-1][r]

        return dp[-1][-1][0] % (10**9 + 7)
