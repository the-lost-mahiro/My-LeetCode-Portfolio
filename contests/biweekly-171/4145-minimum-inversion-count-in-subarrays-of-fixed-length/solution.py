class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        n = len(nums)

        sorted_unique = sorted(set(nums))
        rank_map = {val: i + 1 for i, val in enumerate(sorted_unique)}
        max_rank = len(sorted_unique)
        
        ranks = [rank_map[x] for x in nums]
        
        bit = FenwickTree(max_rank)
        current_inversions = 0
        
        for i in range(k):
            r = ranks[i]
            count_larger = i - bit.query(r)
            current_inversions += count_larger
            bit.update(r, 1)
            
        min_inversions = current_inversions
        
        for i in range(k, n):
            out_rank = ranks[i-k]
            
            bit.update(out_rank, -1)
            
            loss = bit.query(out_rank - 1)
            current_inversions -= loss

            in_rank = ranks[i]

            count_larger = (k - 1) - bit.query(in_rank)
            current_inversions += count_larger
            
            bit.update(in_rank, 1)
            
            min_inversions = min(min_inversions, current_inversions)
            
        return min_inversions
