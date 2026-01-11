class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0
        
        for row in matrix:
            for j in range(n):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            stack = [-1]
            for j in range(n + 1):
                while heights[j] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = j - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(j)
                
        return max_area
