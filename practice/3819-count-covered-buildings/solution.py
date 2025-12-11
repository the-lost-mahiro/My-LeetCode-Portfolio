class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_x = [float('-inf')] * (n + 1)
        max_y = [float('-inf')] * (n + 1)
        min_x = [float('inf')] * (n + 1)
        min_y = [float('inf')] * (n + 1)

        for x, y in buildings:
            max_x[x] = max(y, max_x[x])
            min_x[x] = min(y, min_x[x])
            max_y[y] = max(x, max_y[y])
            min_y[y] = min(x, min_y[y])

        count = 0
        for x, y in buildings:
            if min_x[x] < y < max_x[x] and min_y[y] < x < max_y[y]:
                count += 1

        return count
