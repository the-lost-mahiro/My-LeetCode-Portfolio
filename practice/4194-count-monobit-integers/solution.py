class Solution:
    def countMonobit(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 2
        cnt = 2
        for i in range(3, n + 1, 2):
            if all(s =='1' for s in bin(i)[2:]):
                cnt += 1
        return cnt
