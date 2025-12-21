from collections import Counter, defaultdict

class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        countNums = Counter(nums)
        countForb = Counter(forbidden)
        n = len(nums)
        badPairs = 0
        countPairs = defaultdict(int)

        for i in range(n):
            if nums[i] == forbidden[i]:
                badPairs += 1
                countPairs[nums[i]] += 1

        for key, value in countPairs.items():
            if n - countForb[key] < countNums[key]:
                return -1

        pairsLeft = n - badPairs
        if badPairs == 0:
            return 0
        
        maxBadValueCount = max(countPairs.values())
        return max(math.ceil(badPairs / 2), maxBadValueCount)
