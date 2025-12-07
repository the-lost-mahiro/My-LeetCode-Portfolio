class Solution:
    def largestPrime(self, n: int) -> int:
        def checkPrime(n):
            if n == 2:
                return True
            else:
                for i in range(2, int(n**0.5) + 1):
                    if n % i == 0:
                        return False
                return True
            
        if n <= 1:
            return 0
        elif n == 2:
            return 2
        else:
            start = 3
            total = 2
            pre_total = 2
            while total <= n:
                if checkPrime(start):
                    if pre_total + start <= n:
                        pre_total += start
                        start += 2
                        if checkPrime(pre_total):
                            total = pre_total
                    else:
                        break
                else:
                    if pre_total + start <= n:
                        start += 1
                    else:
                        break
            return total
