class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        for i in range(l):
            if l - i <= ans:
                break
            odd = set()
            even = set()
            for j in range(i, l):
                val = nums[j]
                if val % 2 == 0:
                    even.add(val)
                else:
                    odd.add(val)
                if len(even) == len(odd):
                    ans = max(ans, j - i + 1)    
        return ans
