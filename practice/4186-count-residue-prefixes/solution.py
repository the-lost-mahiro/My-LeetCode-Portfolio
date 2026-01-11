class Solution:
    def residuePrefixes(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            prefix = s[:i + 1]
            if len(set(prefix)) == len(prefix) % 3:
                count += 1
        return count
