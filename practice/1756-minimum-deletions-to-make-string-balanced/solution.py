class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        b = 0
        
        for char in s:
            if char == 'b':
                b += 1
            else:
                if b > 0:
                    res += 1
                    b -= 1
                    
        return res
