class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        limit = [float('inf')] * n
        limit[0] = 0
        
        for idx, val in restrictions:
            limit[idx] = min(limit[idx], val)
            
        for i in range(1, n):
            limit[i] = min(limit[i], limit[i-1] + diff[i-1])
            
        for i in range(n - 2, -1, -1):
            limit[i] = min(limit[i], limit[i+1] + diff[i])
            
        return max(limit)
