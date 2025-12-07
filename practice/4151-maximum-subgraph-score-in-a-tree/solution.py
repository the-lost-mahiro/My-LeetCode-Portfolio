class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        vals = [1 if g == 1 else -1 for g in good]
        
        dp_down = [0] * n
        
        def dfs_down(u, p):
            current_sum = vals[u]
            for v in adj[u]:
                if v == p: continue
                dfs_down(v, u)
                current_sum += max(0, dp_down[v])
            dp_down[u] = current_sum

        dfs_down(0, -1)
        
        ans = [0] * n
        
        def dfs_up(u, p, up_val):
            ans[u] = dp_down[u] + up_val
            
            total_u = ans[u]
            
            for v in adj[u]:
                if v == p: continue
                
                val_without_v = total_u - max(0, dp_down[v])
                
                dfs_up(v, u, max(0, val_without_v))

        dfs_up(0, -1, 0)
        
        return ans
