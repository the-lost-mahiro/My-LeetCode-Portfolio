class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')

        curCount = 0
        for i in range(k):
            if s[i] in vowel:
                curCount += 1

        maxCount = curCount
        for i in range(k, len(s)):
            if s[i - k] in vowel:
                curCount -= 1

            if s[i] in vowel:
                curCount += 1
            
            maxCount = max(maxCount, curCount)
            if maxCount == k:
                return k
        
        return maxCount
