class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7

        minimum = complexity[0]
        for i in range(1, n):
            if complexity[i] <= minimum:
                return 0
            
        result = 1
        for i in range(1, n):
            result = (result * i) % MOD
            
        return result
