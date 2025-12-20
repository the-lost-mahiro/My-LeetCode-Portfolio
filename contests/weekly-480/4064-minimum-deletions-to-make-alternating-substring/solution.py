from typing import List

class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        i += 1 
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def query_range(self, l, r):
        if l > r: return 0
        return self.query(r) - self.query(l - 1)

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        s = list(s)
        n = len(s)
        bit = FenwickTree(n)

        def is_bad(i):
            if 0 <= i < n - 1:
                return 1 if s[i] == s[i+1] else 0
            return 0

        bad_status = [0] * n 
        for i in range(n - 1):
            if s[i] == s[i+1]:
                bad_status[i] = 1
                bit.update(i, 1)

        ans = []
        
        for query in queries:
            if query[0] == 1:
                idx = query[1]

                if idx > 0:
                    bit.update(idx - 1, -bad_status[idx - 1])
                
                if idx < n - 1:
                    bit.update(idx, -bad_status[idx])

                s[idx] = 'B' if s[idx] == 'A' else 'A'
                
                if idx > 0:
                    val = is_bad(idx - 1)
                    bad_status[idx - 1] = val
                    bit.update(idx - 1, val)
                
                if idx < n - 1:
                    val = is_bad(idx)
                    bad_status[idx] = val
                    bit.update(idx, val)
            else:
                l, r = query[1], query[2]
                ans.append(bit.query_range(l, r - 1))
                
        return ans
