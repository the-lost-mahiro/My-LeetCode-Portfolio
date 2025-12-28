class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def get_cost(z):
            c_both = z * costBoth
            c1 = max(0, need1 - z) * cost1
            c2 = max(0, need2 - z) * cost2
            return c_both + c1 + c2
            
        vertices = [0, need1, need2]
        return min(get_cost(z) for z in vertices if z >= 0)
