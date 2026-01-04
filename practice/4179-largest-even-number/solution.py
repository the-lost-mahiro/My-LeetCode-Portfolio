class Solution:
    def largestEven(self, s: str) -> str:
        while len(s) > 0 and s[-1] != '2':
            s = s[0:-1]
        return s
