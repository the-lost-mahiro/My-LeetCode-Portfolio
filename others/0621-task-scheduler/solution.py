from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        freq_max = max(freq)
        n_max = freq.count(freq_max)
        
        return max(len(tasks), (freq_max - 1) * (n + 1) + n_max)
