import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        
        for x in nums:
            divisors = set()
            for d in range(1, int(math.sqrt(x)) + 1):
                if x % d == 0:
                    divisors.add(d)
                    divisors.add(x // d)
                    
                    if len(divisors) > 4:
                        break
            
            if len(divisors) == 4:
                total_sum += sum(divisors)
                
        return total_sum
