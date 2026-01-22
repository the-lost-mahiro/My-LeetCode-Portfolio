class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        def is_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        while not is_sorted(nums):
            min_sum = float('inf')
            best_idx = -1

            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    best_idx = i

            nums[best_idx] = min_sum
            nums.pop(best_idx + 1)
            ans += 1
            
        return ans
