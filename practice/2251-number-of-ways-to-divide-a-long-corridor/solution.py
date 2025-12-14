class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        if not seats or len(seats) & 1:
            return 0
        
        total = 1
        for i in range(2, len(seats), 2):
            length = seats[i] - seats[i - 1]
            total *= length % MOD
        
        return total % MOD
