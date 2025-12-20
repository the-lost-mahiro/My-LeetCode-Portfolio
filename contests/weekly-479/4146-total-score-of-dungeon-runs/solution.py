import bisect

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        
        pref = [0] * (n + 1)
        for k in range(n):
            pref[k+1] = pref[k] + damage[k]
            
        total_score = n * (n + 1) // 2
        
        for j in range(n):
            limit = requirement[j] - hp + pref[j+1]
            
            bad_count = bisect.bisect_left(pref, limit, lo=0, hi=j+1)
            
            total_score -= bad_count
            
        return total_score
