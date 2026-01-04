import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        top_k = []
        heapq.heapify(top_k)

        for num in nums:
            if len(top_k) < k:
                heapq.heappush(top_k, num)
            else:
                heapq.heappush(top_k, num)
                heapq.heappop(top_k)
        
        return top_k[0]
