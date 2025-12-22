class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def backtrack(index, trace, current_sum):
            if current_sum == target:
                ans.append(trace[:])
                return

            if current_sum > target:
                return

            for i in range(index, n):
                trace.append(candidates[i])
                
                backtrack(i, trace, current_sum + candidates[i])
                
                trace.pop()

        backtrack(0, [], 0)
        return ans
