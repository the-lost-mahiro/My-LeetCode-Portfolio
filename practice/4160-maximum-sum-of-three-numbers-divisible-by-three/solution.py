class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        div = {0:0, 1:0, 2:0}
        div2 = {0:[], 1:[], 2:[]}
        
        for num in nums:
            i = num % 3
            div[i] += 1
            div2[i].append(num)

        maxSum = 0
        if div[0] >= 3:
            maxSum = max(maxSum, div2[0][-1] + div2[0][-2] + div2[0][-3])

        if div[1] >= 3:
            maxSum = max(maxSum, div2[1][-1] + div2[1][-2] + div2[1][-3])

        if div[2] >= 3:
            maxSum = max(maxSum, div2[2][-1] + div2[2][-2] + div2[2][-3])

        if div[0] >= 1 and  div[1] >= 1 and div[2] >= 1:
            maxSum = max(maxSum, div2[0][-1] + div2[1][-1] + div2[2][-1])

        return maxSum
