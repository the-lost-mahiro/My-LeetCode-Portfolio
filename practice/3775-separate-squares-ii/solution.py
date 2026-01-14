class UnionSegmentTree:
    def __init__(self, x_coords):
        self.x_coords = x_coords
        self.n = len(x_coords) - 1
        self.tree_cnt = [0] * (4 * self.n)
        self.tree_len = [0.0] * (4 * self.n) 

    def _update_node(self, node, l, r):
        if self.tree_cnt[node] > 0:
            self.tree_len[node] = self.x_coords[r+1] - self.x_coords[l]
        elif l < r:
            self.tree_len[node] = self.tree_len[2 * node] + self.tree_len[2 * node + 1]
        else:
            self.tree_len[node] = 0.0

    def update(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self.tree_cnt[node] += val
            self._update_node(node, l, r)
            return
        
        mid = (l + r) // 2
        if ql <= mid:
            self.update(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        self._update_node(node, l, r)

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        x_set = set()
        for x, y, l in squares:
            x_set.add(x)
            x_set.add(x + l)
        sorted_x = sorted(list(x_set))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        events.sort()

        st = UnionSegmentTree(sorted_x)

        total_area = 0.0
        for i in range(len(events) - 1):
            y, type, x1, x2 = events[i]
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            total_area += st.tree_len[1] * (events[i+1][0] - y)

        target = total_area / 2
        current_area = 0.0
        st = UnionSegmentTree(sorted_x)
        for i in range(len(events) - 1):
            y, type, x1, x2 = events[i]
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            
            slab_area = st.tree_len[1] * (events[i+1][0] - y)
            if current_area + slab_area >= target:
                needed = target - current_area
                return y + (needed / st.tree_len[1])
            current_area += slab_area
            
        return float(events[-1][0])
