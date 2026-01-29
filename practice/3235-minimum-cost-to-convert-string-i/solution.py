class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
            
        for u, v, c in zip(original, changed, cost):
            u_idx, v_idx = ord(u) - ord('a'), ord(v) - ord('a')
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], c)
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        total_cost = 0
        for s, t in zip(source, target):
            if s == t: continue
            res = dist[ord(s) - ord('a')][ord(t) - ord('a')]
            if res == float('inf'): return -1
            total_cost += res
            
        return total_cost
