class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] < nums[m - 1]:
                return nums[m]

            if nums[m] > nums[r]:
                l = m + 1

            else:
                r = m - 1
