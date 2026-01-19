class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                P[r][c] = mat[r-1][c-1] + P[r-1][c] + P[r][c-1] - P[r-1][c-1]
        
        def get_sum(r1, c1, r2, c2):
            return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
        
        def check(k):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if get_sum(r, c, r + k - 1, c + k - 1) <= threshold:
                        return True
            return False
            
        low, high = 1, min(m, n)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
