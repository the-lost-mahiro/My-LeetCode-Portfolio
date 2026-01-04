class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        used = [False] * n

        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False

        backtrack([])
        return ans
