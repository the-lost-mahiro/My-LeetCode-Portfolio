class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        traded = [amount + 1] * (amount + 1)
        traded[0] = 0
        
        for money in range(1, amount + 1):

            for coin in coins:

                if coin <= money:
                        
                        traded[money] = min(traded[money], 1 + traded[money - coin])
        
        return traded[amount] if traded[amount] <= amount else -1
