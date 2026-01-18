class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_p = [[0] * (n + 2) for _ in range(m + 2)]
        col_p = [[0] * (n + 2) for _ in range(m + 2)]
        d1_p = [[0] * (n + 2) for _ in range(m + 2)]
        d2_p = [[0] * (n + 2) for _ in range(m + 2)]
        
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                val = grid[r-1][c-1]
                row_p[r][c] = val + row_p[r][c-1]
                col_p[r][c] = val + col_p[r-1][c]
                d1_p[r][c] = val + d1_p[r-1][c-1]
                d2_p[r][c] = val + d2_p[r-1][c+1]
                
        def is_magic(r, c, k):
            target = row_p[r][c+k-1] - row_p[r][c-1]

            for i in range(r + 1, r + k):
                if row_p[i][c+k-1] - row_p[i][c-1] != target: return False

            for j in range(c, c + k):
                if col_p[r+k-1][j] - col_p[r-1][j] != target: return False

            if d1_p[r+k-1][c+k-1] - d1_p[r-1][c-1] != target: return False
            
            if d2_p[r+k-1][c] - d2_p[r-1][c+k] != target: return False
            
            return True

        for k in range(min(m, n), 1, -1):
            for r in range(1, m - k + 2):
                for c in range(1, n - k + 2):
                    if is_magic(r, c, k):
                        return k
        return 1
