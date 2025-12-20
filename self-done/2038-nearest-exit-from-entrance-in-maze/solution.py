from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        def get_neighbors(node, maze, m, n):
            ways = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            get = []
            for row, col in ways:
                neighbor = (node[0] + row, node[1] + col)
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and maze[neighbor[0]][neighbor[1]] == '.':
                    get.append(neighbor)
            
            return get

        def bfs(start_node, maze, m, n):
            start_node = tuple(start_node)
            queue = deque([start_node])
            visited = set()
            visited.add(start_node)

            steps = 0
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()

                    if (curr[0] == 0 or curr[1] == 0 or curr[0] == m - 1 or curr[1] == n - 1) and curr != start_node:
                        return steps
                    
                    for neighbor in get_neighbors(curr, maze, m, n):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                    
                steps += 1

            return -1
        
        return bfs(entrance, maze, m, n)
