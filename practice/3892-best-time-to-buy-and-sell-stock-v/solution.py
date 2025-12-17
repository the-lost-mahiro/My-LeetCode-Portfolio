class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        
        dp = [[0] * 3 for _ in range(k + 1)]
        
        for rem_k in range(k + 1):
            dp[rem_k][1] = float('-inf')
            dp[rem_k][2] = float('-inf')

        for price in reversed(prices):
            new_dp = [[0] * 3 for _ in range(k + 1)]

            for rem_k in range(1, k + 1):
                new_dp[rem_k][0] = max(
                    dp[rem_k][0], 
                    -price + dp[rem_k][1], 
                    price + dp[rem_k][2]
                )

                new_dp[rem_k][1] = max(
                    dp[rem_k][1],
                    price + dp[rem_k - 1][0]
                )

                new_dp[rem_k][2] = max(
                    dp[rem_k][2],
                    -price + dp[rem_k - 1][0]
                )
            
            dp = new_dp

        return dp[k][0]
