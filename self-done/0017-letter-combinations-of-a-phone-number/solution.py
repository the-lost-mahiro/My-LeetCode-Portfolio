class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = [['a', 'b', 'c'], ['d', 'e' ,'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        ans = []
        s = ''
        n = 0
        def mix(ans, phone, digits, s, n):
            if len(s) == len(digits):
                ans.append(s)
                return
            
            for i in range(len(phone[int(digits[n]) - 2])):
                head = phone[int(digits[n]) - 2][i]
                mix(ans, phone, digits, s + head, n + 1)

        mix(ans, phone, digits, s, n)
        return ans
