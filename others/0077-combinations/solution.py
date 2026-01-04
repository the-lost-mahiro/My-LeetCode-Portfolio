class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(index, trace, length):
            if length == k:
                ans.append(trace[:])
                return
            
            for i in range(index, n):
                trace.append(i + 1)
                backtrack(i + 1, trace, length + 1)
                trace.pop()
            
        backtrack(0, [], 0)

        return ans
