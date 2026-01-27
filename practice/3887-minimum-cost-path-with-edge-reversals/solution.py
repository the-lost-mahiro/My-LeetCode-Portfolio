from collections import defaultdict
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w * 2])
        
        def dijkstra(n, adj, source):
            distances = [float('inf')] * n
            distances[source] = 0
            pq = [(0, source)]
            
            while pq:
                current_dist, u = heapq.heappop(pq)

                if current_dist > distances[u]:
                    continue

                for v, weight in adj[u]:
                    distance = current_dist + weight

                    if distance < distances[v]:
                        distances[v] = distance
                        heapq.heappush(pq, (distance, v))
            
            return distances[n - 1] if distances[n - 1] != float('inf') else -1
        
        return dijkstra(n, adj, 0)
