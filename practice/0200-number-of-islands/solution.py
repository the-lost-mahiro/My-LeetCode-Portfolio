from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        seen = set()
        neighbors = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(start_node):
            queue = deque()

            # if start_node not in seen:
            #     queue.append(start_node)
            #     seen.add(start_node)

            queue.append(start_node)
            
            while queue:
                x, y = queue.popleft()
                
                if grid[x][y] == '1':
                    for a, b in neighbors:
                        if 0 <= x + a < m and 0 <= y + b < n:
                            neighbor = (x + a, y + b)

                            if neighbor not in seen and grid[x + a][y + b] == '1':
                                queue.append(neighbor)
                                seen.add(neighbor)
            
            return
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    islands += 1
                    bfs((i, j))
                    seen.add((i, j))

        return islands
