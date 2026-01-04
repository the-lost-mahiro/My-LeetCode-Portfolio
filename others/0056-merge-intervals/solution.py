class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        merged = []
        
        prev = intervals[0]
        for i in range(1, n):
            curr = intervals[i]

            if prev[1] >= curr[0]:
                curr = [min(curr[0], prev[0]), max(curr[1], prev[1])]
                prev = curr
            
            else:
                merged.append(prev)
                prev = curr
        
        merged.append(prev)
        
        return merged
