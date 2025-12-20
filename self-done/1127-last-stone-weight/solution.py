import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                return -stones[0]
            heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
            
        return 0
