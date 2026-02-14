class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cup = [[0] * (r + 1) for r in range(101)]
        cup[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                pour = (cup[r][c] - 1) / 2

                if pour > 0:
                    cup[r + 1][c] += pour
                    cup[r + 1][c + 1] += pour
                
        return min(1, cup[query_row][query_glass])
