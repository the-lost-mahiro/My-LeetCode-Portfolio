from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = set()

        def dfs(node):
            if node == destination:
                return True
            
            seen.add(node)

            for neighbor in adj[node]:
                if neighbor not in seen:
                    if dfs(neighbor):
                        return True
            
            return False

        return dfs(source)
