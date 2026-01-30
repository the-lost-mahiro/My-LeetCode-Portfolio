import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        lengths = sorted(list(set(len(s) for s in original)))

        adj = defaultdict(list)
        nodes = set()
        for u, v, c in zip(original, changed, cost):
            adj[u].append((v, c))
            nodes.add(u)
            nodes.add(v)
            
        dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for start_node in nodes:
            dist[start_node][start_node] = 0
            pq = [(0, start_node)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[start_node][u]: continue
                for v, c in adj[u]:
                    if d + c < dist[start_node][v]:
                        dist[start_node][v] = d + c
                        heapq.heappush(pq, (dist[start_node][v], v))

        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == float('inf'): continue

            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])

            for L in lengths:
                if i + L > n: break
                sub_s = source[i : i+L]
                sub_t = target[i : i+L]

                if sub_s in dist and sub_t in dist[sub_s]:
                    cost_val = dist[sub_s][sub_t]
                    if dp[i] + cost_val < dp[i+L]:
                        dp[i+L] = dp[i] + cost_val
                        
        return dp[n] if dp[n] != float('inf') else -1
