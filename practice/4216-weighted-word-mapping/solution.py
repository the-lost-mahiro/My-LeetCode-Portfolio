class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ''
            
        for w in words:
            total = 0
            
            for c in w:
                total += weights[(ord(c) - 97)]

            total %= 26
            ans += chr(122 - total)

        return ans
