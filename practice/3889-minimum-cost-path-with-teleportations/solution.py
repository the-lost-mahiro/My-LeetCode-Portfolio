from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        dp[0][0] = 0

        for r in range(m):
            for c in range(n):
                if r > 0: dp[r][c] = min(dp[r][c], dp[r-1][c] + grid[r][c])
                if c > 0: dp[r][c] = min(dp[r][c], dp[r][c-1] + grid[r][c])
        
        for _ in range(k):
            val_to_min_cost = defaultdict(lambda: float('inf'))
            for r in range(m):
                for c in range(n):
                    if dp[r][c] != float('inf'):
                        v = grid[r][c]
                        val_to_min_cost[v] = min(val_to_min_cost[v], dp[r][c])
            
            if not val_to_min_cost: break
            
            sorted_vals = sorted(val_to_min_cost.keys(), reverse=True)
            suffix_min_map = {}
            curr_min = float('inf')
            for v in sorted_vals:
                curr_min = min(curr_min, val_to_min_cost[v])
                suffix_min_map[v] = curr_min
            
            new_dp = [row[:] for row in dp]
            
            for r in range(m):
                for c in range(n):
                    v = grid[r][c]
                    if v in suffix_min_map:
                        new_dp[r][c] = min(new_dp[r][c], suffix_min_map[v])
                    elif sorted_vals and v < sorted_vals[-1]:
                        new_dp[r][c] = min(new_dp[r][c], curr_min)

            for r in range(m):
                for c in range(n):
                    if r > 0: new_dp[r][c] = min(new_dp[r][c], new_dp[r-1][c] + grid[r][c])
                    if c > 0: new_dp[r][c] = min(new_dp[r][c], new_dp[r][c-1] + grid[r][c])
            
            dp = new_dp
            
        return dp[m-1][n-1]
