import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        candidates = []

        for length in range(1, 21):
            half_len = (length + 1) // 2

            start = 1 << (half_len - 1)
            end = (1 << half_len) - 1
            
            for i in range(start, end + 1):
                s = bin(i)[2:] 
                
                if length % 2 == 1:
                    full_bin = s + s[:-1][::-1]
                else:
                    full_bin = s + s[::-1]
                
                candidates.append(int(full_bin, 2))
        
        candidates.sort()
        
        ans = []
        for x in nums:
            idx = bisect.bisect_left(candidates, x)
            
            min_ops = float('inf')
            
            if idx < len(candidates):
                min_ops = min(min_ops, candidates[idx] - x)
            
            if idx > 0:
                min_ops = min(min_ops, x - candidates[idx-1])
                
            ans.append(min_ops)
            
        return ans
