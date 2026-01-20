class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for num in nums:
            if num == 2:
                ans.append(-1)

            else:
                trail = num & ~(num + 1)
                max_bit = 1 << (trail.bit_length() - 1)
                ans.append(num - max_bit)
            
        return ans
