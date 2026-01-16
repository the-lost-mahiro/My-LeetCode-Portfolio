class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        MOD = 10**9 + 7

        h_distances = set()
        for i in range(len(hFences) - 1):
            for j in range(i + 1, len(hFences)):
                h_distances.add(abs(hFences[i] - hFences[j]))
        
        max_side = -1
        for i in range(len(vFences) - 1):
            for j in range(i + 1, len(vFences)):
                cur_side = abs(vFences[i] - vFences[j])
                if cur_side in h_distances:
                    max_side = max(max_side, cur_side)
        
        return max_side ** 2 % MOD if max_side != -1 else -1
