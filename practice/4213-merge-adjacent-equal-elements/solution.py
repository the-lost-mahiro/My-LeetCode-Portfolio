class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []

        for i, num in enumerate(nums):               
            while len(stack) and stack[-1] == num:
                num = stack.pop() * 2

            stack.append(num)

        return stack
