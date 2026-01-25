class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start):
            queue = deque([start])
            dist = [-1] * n
            dist[start] = 0
            while queue:
                node = queue.popleft()

                for neighbor in adj[node]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)

            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)

        count = 0
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])
            if a * a + b * b == c * c:
                count += 1

        return count
