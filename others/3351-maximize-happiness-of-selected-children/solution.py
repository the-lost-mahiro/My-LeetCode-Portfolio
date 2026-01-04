class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)

        happinessSum = 0
        decrease = 0
        for i in range(k):
            cur = happiness[i] - decrease
            
            if cur <= 0:
                return happinessSum

            happinessSum += cur
            decrease += 1

        return happinessSum
