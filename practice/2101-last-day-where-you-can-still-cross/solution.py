class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        neighbors = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(node):
            if node[0] == row - 1:
                return True
            
            seen.add(node)

            for nr, nc in neighbors:
                if 0 <= node[0] + nr < row and 0 <= node[1] + nc < col:
                    neighbor = (node[0] + nr, node[1] + nc)
                    if neighbor not in seen and dfs(neighbor):
                        return True
            
            return False

        left = 0
        right = len(cells) - 1
        day = 0
        while left <= right:
            mid = (left + right) // 2

            n_cells = cells[0 : mid + 1]

            seen = set()

            for nr, nc in n_cells:
                seen.add((nr - 1, nc - 1))
            
            path = False
            for c in range(col):
                node = (0, c)

                if node not in seen:
                    if dfs(node):
                        path = True
                        break
                    
            if path:
                left = mid + 1
                day = left

            else:
                right = mid - 1
        
        return day
