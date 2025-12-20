class Solution:
    def completePrime(self, num: int) -> bool:
        def checkPrime(n: int):
            if n <= 1:
                return False
    
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
                
            return True
        
        sur = num % 10
        pre = num // (10 ** (len(str(num)) - 1))
    
        check = True
        for i in range(1, len(str(num)) + 1):
            sur = num % (10 ** i)
            pre = num // (10 ** (i - 1))
    
            if not checkPrime(sur) or not checkPrime(pre):
                check = False
    
        return check
