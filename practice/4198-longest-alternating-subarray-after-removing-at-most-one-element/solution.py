class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        dpLi, dpLd, dpRi, dpRd = [1] * n, [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                dpLi[i] = dpLd[i - 1] + 1
            elif nums[i - 1] < nums[i]:
                dpLd[i] = dpLi[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dpRd[i] = dpRi[i + 1] + 1
            elif nums[i] > nums[i + 1]:
                dpRi[i] = dpRd[i + 1] + 1
                
        maxi = max(max(dpLi), max(dpLd), max(dpRi), max(dpRd))
        
        for i in range(1, n - 1):
            if nums[i - 1] > nums[i + 1]:
                maxi = max(maxi, dpLd[i - 1] + dpRd[i + 1])
            elif nums[i - 1] < nums[i + 1]:
                maxi = max(maxi, dpLi[i - 1] + dpRi[i + 1])

        return maxi
