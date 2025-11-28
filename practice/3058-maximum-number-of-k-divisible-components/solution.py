class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
        stack = [0]
        parent = [-1] * n
        order = [] 
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            order.append(u)    
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    stack.append(v)
        component_count = 0
        current_values = list(values)
        for i in range(n - 1, -1, -1):
            node = order[i]
            val = current_values[node]
            if val % k == 0:
                component_count += 1
            else:
                p = parent[node]
                if p != -1:
                    current_values[p] += val
        return component_count
