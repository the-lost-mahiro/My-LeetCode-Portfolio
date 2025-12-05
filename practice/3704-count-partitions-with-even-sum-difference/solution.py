class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n):
            left = nums[0:i]
            right = nums[i:n]
            if (sum(left) - sum(right)) % 2 == 0:
                count += 1 
        
        return count
