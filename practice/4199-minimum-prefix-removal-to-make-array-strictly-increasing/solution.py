class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        length = 1
        cur = nums[-1]
        for i in range(n - 2, -1, -1):
            if cur > nums[i]:
                cur = nums[i]
                length += 1
            else:
                break
        return n - length
