class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = len(prices)
        pre = prices[0]
        stack = 1
        
        for i in range(1, len(prices)):
            cur = prices[i] 
            if cur - pre == -1:
               stack += 1
            else:
               total += (stack * (stack - 1)) // 2
               stack = 1
            cur, pre = pre, cur
        total += (stack * (stack - 1)) // 2
        
        return total
