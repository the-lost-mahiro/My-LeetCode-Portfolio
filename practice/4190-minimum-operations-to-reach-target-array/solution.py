class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        count = Counter(nums)
        max_ops = len(count)

        for i in range(len(nums)):
            if nums[i] == target[i]:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    max_ops -= 1

        return max_ops
