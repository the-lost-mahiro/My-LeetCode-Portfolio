class Solution:
    def lastInteger(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        is_op1 = True
        
        while remaining > 1:
            if not is_op1 and remaining % 2 == 0:
                head += step

            step *= 2
            remaining = (remaining + 1) // 2
            is_op1 = not is_op1
            
        return head
