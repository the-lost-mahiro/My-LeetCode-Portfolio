import heapq

class Node:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
        self.prev = None
        self.next = None
        self.removed = False

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        nodes = [Node(v, i) for i, v in enumerate(nums)]
        for i in range(n):
            if i > 0: nodes[i].prev = nodes[i-1]
            if i < n - 1: nodes[i].next = nodes[i+1]

        def is_inv(a, b):
            if not a or not b: return 0
            return 1 if a.val > b.val else 0

        total_inversions = 0
        for i in range(n - 1):
            total_inversions += is_inv(nodes[i], nodes[i+1])
            
        if total_inversions == 0: return 0

        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nodes[i].val + nodes[i+1].val, nodes[i].pos, nodes[i], nodes[i+1]))

        ans = 0
        while total_inversions > 0 and pq:
            s, pos, left, right = heapq.heappop(pq)

            if left.removed or right.removed or left.next != right:
                continue

            p = left.prev
            nn = right.next

            inv_before = is_inv(p, left) + is_inv(left, right) + is_inv(right, nn)

            new_val = left.val + right.val
            new_node = Node(new_val, left.pos)
            
            new_node.prev = p
            new_node.next = nn
            if p: p.next = new_node
            if nn: nn.prev = new_node
            
            left.removed = right.removed = True
            ans += 1
            
            inv_after = is_inv(p, new_node) + is_inv(new_node, nn)
            total_inversions += (inv_after - inv_before)

            if p:
                heapq.heappush(pq, (p.val + new_node.val, p.pos, p, new_node))
            if nn:
                heapq.heappush(pq, (new_node.val + nn.val, new_node.pos, new_node, nn))
                
        return ans
