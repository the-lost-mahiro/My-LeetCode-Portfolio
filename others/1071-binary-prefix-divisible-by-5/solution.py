class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        new_value = 0
        for i in range(len(nums)):
            new_value = (new_value*2 + nums[i])%5
            if new_value == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
