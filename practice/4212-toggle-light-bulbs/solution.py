class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = Counter(bulbs)
        ans = [k for k, v in on.items() if v % 2 != 0]
        return sorted(ans)
