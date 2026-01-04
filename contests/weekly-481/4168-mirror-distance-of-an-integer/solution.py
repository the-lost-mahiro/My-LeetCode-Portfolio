class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n - int(''.join(reversed(str(n)))))
