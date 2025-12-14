class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = set(['a', 'i', 'e', 'u', 'o'])
        s = s.split()
        first = 0
        
        for i, word in enumerate(s):
            if i == 0:
                for char in word:
                    if char in vowels:
                        first += 1

            else:
                count = 0
                for char in word:
                    if char in vowels:
                        count += 1
                        
                if count == first:
                    s[i] = word[::-1]

        return ' '.join(s)
