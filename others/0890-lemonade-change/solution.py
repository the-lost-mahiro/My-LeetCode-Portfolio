from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        charge = defaultdict(int)

        for bill in bills:

            if bill == 5:
                charge[5] += 1
            
            elif bill == 10:

                if charge[5] == 0:
                    return False
                
                else:
                    charge[5] -= 1
                    charge[10] += 1
            
            else:
                if charge[5] == 0:
                    return False

                if charge[10] > 0:
                    charge[5] -= 1
                    charge[10] -= 1

                else:
                    if charge[5] < 3:
                        return False
                    
                    else:
                        charge[5] -= 3
        
        return True
