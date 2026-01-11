from collections import defaultdict

class Solution:
    def countPairs(self, words: List[str]) -> int:
        caesar = defaultdict(int)

        for word in words:
            org_word = ''
            shift = ord(word[0]) - 97
            for char in word:
                org_word += chr((ord(char) - 97 - shift) % 26 + 97)
            caesar[org_word] += 1

        result = 0
        for val in caesar.values():
            result += val * (val - 1) // 2

        return result
