class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            current_sum = 0
            seen = set()
            for j in range(i,n):
                current_sum += nums[j]
                seen.add(nums[j])

                if current_sum in seen:
                    count += 1

        return count
