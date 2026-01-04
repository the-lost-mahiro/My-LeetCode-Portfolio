from collections import defaultdict

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        charCost = defaultdict(int)
        totalCost = sum(cost)
        
        for i, char in enumerate(s):
            charCost[char] += cost[i]

        minCost = float('inf')
        curCost = 0
        for key, value in charCost.items():
            curCost = totalCost - value
            minCost = min(minCost, curCost)

        return minCost
