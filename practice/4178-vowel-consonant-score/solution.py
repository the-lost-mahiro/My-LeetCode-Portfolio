class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel = set('aeiou')
        v = 0
        c = 0
        
        for char in s:
            if char in vowel:
                v += 1
            elif char.isalpha():
                c += 1

        return v // c if c else 0
