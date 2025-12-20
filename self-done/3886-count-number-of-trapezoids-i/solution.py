class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        lines = {}

        for point in points:
            if point[1] not in lines:
                lines[point[1]] = 1
            else:
                lines[point[1]] += 1

        sum_val = 0
        sum_val_sq = 0
        for y in lines.values():
            val = y * (y - 1) // 2
            sum_val += val
            sum_val_sq += val * val

        result = (sum_val * sum_val - sum_val_sq) // 2
        return result % MOD
