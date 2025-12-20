class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        freqPrev = {}
        freqNext = {}
        triplets = 0
        MOD = 10**9 + 7

        for i in range(1, n):
            if nums[i] not in freqNext:
                freqNext[nums[i]] = 1
            else:
                freqNext[nums[i]] += 1
        
        for j in range(n - 1):
            num = nums[j] * 2
            if num in freqPrev and num in freqNext:
                triplets += (freqPrev[num] * freqNext[num]) % MOD

            if nums[j] not in freqPrev:
                freqPrev[nums[j]] = 1
            else:
                freqPrev[nums[j]] += 1
            freqNext[nums[j + 1]] -= 1

        return triplets % MOD
