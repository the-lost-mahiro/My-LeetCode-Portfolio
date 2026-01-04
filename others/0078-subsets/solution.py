class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = []

        def backtrack(index, path):
            nonlocal n
            subset.append(path[:])
            
            if index == n:
                return
            
            for i in range(index, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        
        return subset
