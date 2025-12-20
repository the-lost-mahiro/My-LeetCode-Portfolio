class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] in seen:
                return (i // 3) + 1
            seen.add(nums[i])
        return 0
