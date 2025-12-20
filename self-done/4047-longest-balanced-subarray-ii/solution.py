class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.min_val = [0] * (4 * n)
        self.max_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def push(self, node):
        if self.lazy[node] != 0:
            lz = self.lazy[node]

            self.lazy[2 * node] += lz
            self.min_val[2 * node] += lz
            self.max_val[2 * node] += lz

            self.lazy[2 * node + 1] += lz
            self.min_val[2 * node + 1] += lz
            self.max_val[2 * node + 1] += lz

            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        if l <= start and end <= r:
            self.lazy[node] += val
            self.min_val[node] += val
            self.max_val[node] += val
            return
        
        self.push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])


    def find_last_zero(self, node, start, end, query_l):
        if end < query_l or self.min_val[node] > 0 or self.max_val[node] < 0:
            return -1
        
        if start == end:
            return start if self.min_val[node] == 0 else -1
        
        self.push(node)
        mid = (start + end) // 2
        
        res = self.find_last_zero(2 * node + 1, mid + 1, end, query_l)
        if res != -1:
            return res
        
        return self.find_last_zero(2 * node, start, mid, query_l)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import deque
        
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = deque()
            pos[x].append(i)
            
        st = SegmentTree(n)

        visited_init = set()
        for i, x in enumerate(nums):
            if x not in visited_init:
                sign = 1 if x % 2 != 0 else -1
                st.update(1, 0, n - 1, i, n - 1, sign)
                visited_init.add(x)
        
        ans = 0
        
        last_zero = st.find_last_zero(1, 0, n - 1, 0)
        if last_zero != -1:
            ans = last_zero + 1 
            
        for l in range(n):
            val = nums[l]
            sign = 1 if val % 2 != 0 else -1
            

            occurrences = pos[val]
            current_idx = occurrences.popleft() 
            
            if occurrences:
                next_idx = occurrences[0]
            else:
                next_idx = n
            
            st.update(1, 0, n - 1, l, next_idx - 1, -sign)
            
            if l + 1 < n:
                last_zero = st.find_last_zero(1, 0, n - 1, l + 1)
                if last_zero != -1:
                    ans = max(ans, last_zero - (l + 1) + 1)
                    
        return ans
