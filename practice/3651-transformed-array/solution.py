class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + val) % len(nums)] for i, val in enumerate(nums)] 
