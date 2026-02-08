from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        ans = 0
        l = 0

        for r, n in enumerate(nums):
            while maxQueue and maxQueue[-1] < n:
                maxQueue.pop()
                
            maxQueue.append(n)

            while minQueue and minQueue[-1] > n:
                minQueue.pop()
                
            minQueue.append(n)

            while (maxQueue[0] - minQueue[0]) * (r - l + 1) > k:
                if nums[l] == maxQueue[0]:
                    maxQueue.popleft()
                    
                if nums[l] == minQueue[0]:
                    minQueue.popleft()
                    
                l += 1

            ans += r - l + 1

        return ans
