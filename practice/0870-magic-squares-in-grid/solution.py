class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if m >= 3 and n >=3:
            magic_squares_lookup = {
                ((8, 1, 6), (3, 5, 7), (4, 9, 2)): True,
                ((6, 1, 8), (7, 5, 3), (2, 9, 4)): True,
                ((4, 9, 2), (3, 5, 7), (8, 1, 6)): True,
                ((2, 9, 4), (7, 5, 3), (6, 1, 8)): True,
                ((8, 3, 4), (1, 5, 9), (6, 7, 2)): True,
                ((4, 3, 8), (9, 5, 1), (2, 7, 6)): True,
                ((6, 7, 2), (1, 5, 9), (8, 3, 4)): True,
                ((2, 7, 6), (9, 5, 1), (4, 3, 8)): True
            }

            def check_square(square):
                key = tuple(tuple(row) for row in square)
                return magic_squares_lookup.get(key, False)
            
            count = 0
            i = 0
            while i < m - 2:
                j = 0

                while j < n - 2:
                    if grid[i + 1][j + 1] == 5:
                        square = [grid[i][j : j + 3], grid[i + 1][j : j + 3], grid[i + 2][j : j + 3]]

                        if check_square(square):
                            count += 1

                    j += 1
                
                i += 1
            
            return count

        else:
            return 0
