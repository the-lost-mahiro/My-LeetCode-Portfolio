class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        ans = []
        diff = float('inf')

        for i in range(len(arr) - 1):

            cur_diff = arr[i + 1] - arr[i]

            if cur_diff < diff:
                diff = cur_diff
                ans = [[arr[i], arr[i + 1]]]

            elif cur_diff == diff:
                ans.append([arr[i], arr[i + 1]])

        return ans
