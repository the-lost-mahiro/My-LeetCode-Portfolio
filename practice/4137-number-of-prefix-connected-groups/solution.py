class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        nwords = []
        for w in words:
            if len(w) >= k:
                nwords.append(w[:k])
        nwords.sort()
        seen = set()
        for i, j in pairwise(nwords):
            if i == j and i not in seen:
                seen.add(i)
        return len(seen)
