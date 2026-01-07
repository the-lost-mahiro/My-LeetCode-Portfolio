class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefixSum = [0] * (n + 1)

        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + gain[i]
        
        return max(prefixSum)
