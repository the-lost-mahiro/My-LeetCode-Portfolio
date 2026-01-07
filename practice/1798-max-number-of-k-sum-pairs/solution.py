from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        pairs = 0

        for key in count.keys():
            while count[key] > 0:
                count[key] -= 1
                target = k - key
                if count[target] > 0:
                    count[target] -= 1
                    pairs += 1
                else:
                    break
        
        return pairs
