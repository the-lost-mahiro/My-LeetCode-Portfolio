from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        matrix = [tuple(row) for row in grid]
        count = Counter(matrix)

        pairs = 0
        for c in range(len(grid)):
            col = []
            for r in range(len(grid)):
                col.append(grid[r][c])
            col = tuple(col)
            if col in count:
                pairs += count[col]
        
        return pairs
