from collections import defaultdict, deque
from itertools import combinations

class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        graph = defaultdict(set)
        
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        totalGroupCounts = Counter(group)
        self.totalCost = 0

        def dfs(curr, prev):
            currSubtreeCounts = {group[curr]: 1}
            
            for neighbor in graph[curr]:
                if neighbor == prev:
                    continue
                
                childSubtreeCounts = dfs(neighbor, curr)
                
                for g_id, countInChild in childSubtreeCounts.items():
                    countOutside = totalGroupCounts[g_id] - countInChild
                    self.totalCost += countInChild * countOutside
                
                if len(childSubtreeCounts) > len(currSubtreeCounts):
                    currSubtreeCounts, childSubtreeCounts = childSubtreeCounts, currSubtreeCounts
                
                for g_id, count in childSubtreeCounts.items():
                    currSubtreeCounts[g_id] = currSubtreeCounts.get(g_id, 0) + count
            
            return currSubtreeCounts

        dfs(0, -1)
        return self.totalCost
