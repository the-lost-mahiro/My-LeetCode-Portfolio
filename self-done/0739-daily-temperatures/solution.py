class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        index_stack = []

        for i in range(n - 1, -1, -1):
            while index_stack and temperatures[i] >= temperatures[index_stack[-1]]:
                index_stack.pop()
        
            if index_stack:
                answer[i] = index_stack[-1] - i

            index_stack.append(i)

        return answer
