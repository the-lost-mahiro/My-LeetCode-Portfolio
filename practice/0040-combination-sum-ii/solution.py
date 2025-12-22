class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        n = len(candidates)

        def backtrack(index, trace, current_sum):
            if current_sum == target:
                ans.append(trace[:])
                return

            if current_sum > target:
                return

            for i in range(index, n):
                
                if current_sum + candidates[i] > target:
                    break

                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                trace.append(candidates[i])
                
                backtrack(i + 1, trace, current_sum + candidates[i])
                
                trace.pop()

        backtrack(0, [], 0)
        return ans
