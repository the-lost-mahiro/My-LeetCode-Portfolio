class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = int((a**2 + b**2 + 1)**0.5)
                if c <= n and c**2 == a**2 + b**2:
                    count += 1
        return count
