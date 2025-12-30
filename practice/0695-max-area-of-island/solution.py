from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()
        neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(start_node, area):
            queue = deque()

            queue.append(start_node)
            seen.add(start_node)
            
            while queue:
                x, y = queue.popleft()
                
                for a, b in neighbors:
                    if 0 <= x + a < m and 0 <= y + b < n:
                        neighbor = (x + a, y + b)

                        if neighbor not in seen and grid[x + a][y + b] == 1:
                            queue.append(neighbor)
                            seen.add(neighbor)
                            area += 1
            
            return area
        
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in seen:
                    cur_area = bfs((i, j), 1)
                    max_area = max(cur_area, max_area)

        return max_area
