class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        del_col = 0

        finState = [False for _ in range(rows - 1)]

        for c in range(0, cols):
            curState = finState[:]
            update = True
            
            for r in range(1, rows):
                if curState[r - 1]:
                    continue

                elif strs[r - 1][c] > strs[r][c]:                    
                    del_col += 1
                    update = False
                    break
                
                elif strs[r - 1][c] < strs[r][c]:
                    curState[r - 1] = True

            if update:
                finState = curState

        return del_col
