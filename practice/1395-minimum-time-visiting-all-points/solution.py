class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        prev_x, prev_y = points[0]
        for i in range(1, len(points)):
            curr_x, curr_y = points[i]
            time += max(abs(curr_x - prev_x), abs(curr_y - prev_y))
            prev_x, prev_y = points[i]
        return time
