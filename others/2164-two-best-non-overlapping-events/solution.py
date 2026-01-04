from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        suffixMax = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(events[i][2], suffixMax[i + 1])
            
        ans = 0
        
        start_times = [e[0] for e in events]
        
        for i in range(n):
            startTime, endTime, value = events[i]
            idx = bisect_right(start_times, endTime)
            
            ans = max(ans, value + suffixMax[idx])
            
        return ans
