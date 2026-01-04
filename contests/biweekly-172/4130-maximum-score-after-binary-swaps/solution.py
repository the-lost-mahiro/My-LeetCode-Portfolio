import heapq

class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        max_heap = []
        total_score = 0
        
        for i in range(len(nums)):
            heapq.heappush(max_heap, -nums[i])
            
            if s[i] == '1':
                total_score += -heapq.heappop(max_heap)
                
        return total_score
