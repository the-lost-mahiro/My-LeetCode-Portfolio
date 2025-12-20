class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        l = 0
        r = k - 1
        l_mod = k // 2 
        sum_org = 0
        sum_mod = 0
        sum_all = 0
        
        for i in range(n):
            sum_all += prices[i] * strategy[i]
        
        for i in range(k):
            sum_org += prices[i] * strategy[i]
            if i >= l_mod:
                sum_mod += prices[i]
        
        total = max(sum_all, sum_all + sum_mod - sum_org)
        
        for _ in range(1, n - k + 1):
            sum_org = sum_org - (prices[l] * strategy[l]) + (prices[r + 1] * strategy[r + 1])
            sum_mod = sum_mod - prices[l_mod] + prices[r + 1]
            
            l += 1
            r += 1
            l_mod += 1
            
            total = max(total, sum_all + sum_mod - sum_org)

        return total
