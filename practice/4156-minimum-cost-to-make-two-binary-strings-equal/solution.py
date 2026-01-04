class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        typeA = 0 # s=1, t=0
        typeB = 0 # s=0, t=1
        
        for c1, c2 in zip(s, t):
            if c1 == '1' and c2 == '0': typeA += 1
            if c1 == '0' and c2 == '1': typeB += 1
            
        ans = 0
        
        pairs = min(typeA, typeB)
        ans += pairs * min(swapCost, 2 * flipCost)
        
        remain = abs(typeA - typeB)
        
        ans += (remain // 2) * min(2 * flipCost, crossCost + swapCost)
        
        if remain % 2 == 1:
            ans += flipCost
            
        return ans
