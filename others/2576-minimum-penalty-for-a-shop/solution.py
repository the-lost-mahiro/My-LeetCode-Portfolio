class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curScore = 0
        maxScore = 0
        closeHour = -1

        for i, cus in enumerate(customers):
    
            if cus == 'Y':
                curScore -= 1

            else:
                curScore += 1

            if curScore < maxScore:
                maxScore = curScore
                closeHour = i
        
        return closeHour + 1
