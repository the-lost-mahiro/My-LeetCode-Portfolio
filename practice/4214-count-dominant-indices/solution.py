class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        surfixAvg = [0] * n
        surfixAvg[-1] = nums[-1]

        l = 1
        cnt = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > surfixAvg[i + 1]:
                cnt += 1
            surfixAvg[i] = (surfixAvg[i + 1] * l + nums[i]) / (l + 1)
            l += 1

        return cnt
