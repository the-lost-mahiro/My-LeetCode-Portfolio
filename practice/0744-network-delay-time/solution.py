from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        distances = [float('inf')] * n
        distances[k - 1] = 0

        hp = [(0, k)]
        heapq.heapify(hp)

        while hp:
            current_dist, u = heapq.heappop(hp)

            if current_dist > distances[u - 1]:
                continue
            
            for v, weight in adj[u]:
                distance = current_dist + weight
                if distance < distances[v - 1]:
                    distances[v - 1] = distance
                    heapq.heappush(hp, (distance, v))
        
        return max(distances) if float('inf') not in distances else -1
