class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        diff = []
        positive = 0
        for i in range(n):
            a = technique1[i] - technique2[i]
            diff.append(a)
            if a > 0:
                positive += 1
            
        pair = sorted(zip(diff, technique1, technique2), reverse=True)
        sort_diff, sort_tech1, sort_tech2 = zip(*pair)
    
        if positive >= k:
            total = sum(sort_tech1[:positive] + sort_tech2[positive:])
        else:
            total = sum(sort_tech1[:positive] + sort_tech1[positive:positive + (k - positive)] + sort_tech2[positive + (k - positive):])
        
        return total
