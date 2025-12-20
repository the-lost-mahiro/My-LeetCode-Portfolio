class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        neg = 0
        req = 0

        if sum(balance) < 0:
            return -1
        
        for i, num in enumerate(balance):
            if num < 0:
                neg = i
                req = abs(num)

        if req == 0:
            return 0
        
        waste = 1
        steps = 0
        while True:
            if n & 1:
                total = (balance[(neg - waste) % n] + balance[(neg + waste) % n])
                
                if total < req:
                    steps += total * waste
                    waste += 1
                    req -= total
                elif total == req:
                    steps += total * waste
                    return steps
                else:
                    steps += req * waste
                    return steps

            else:
                if waste == n // 2:
                    total = balance[(neg - waste) % n] * waste
                    
                    if total == req:
                        steps += total
                        return steps
                    else:
                        steps += req * waste
                        return steps

                else:
                    total = (balance[(neg - waste) % n] + balance[(neg + waste) % n])
                    
                    if total < req:
                        steps += total * waste
                        waste += 1
                        req -= total
                    elif total == req:
                        steps += total * waste
                        return steps
                    else:
                        steps += req * waste
                        return steps
