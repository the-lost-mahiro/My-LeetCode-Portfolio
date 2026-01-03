from collections import defaultdict

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        curSum = 0
        minLength = float('inf')

        l = 0
        for r in range(len(nums)):
            n = nums[r]
            
            if counter[n] == 0:
                curSum += n
            counter[n] += 1                

            while curSum >= k:
                minLength = min(minLength, r - l + 1)
                leftVal = nums[l]

                if counter[leftVal] == 1:
                    curSum -= leftVal

                counter[leftVal] -= 1
                l += 1

        return minLength if minLength != float('inf') else -1
