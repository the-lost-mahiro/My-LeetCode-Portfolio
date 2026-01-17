class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        max_qual = -1
        min_coor = [-1, -1]

        for x, y, qual in towers:
            dist = abs(center[0] - x) + abs(center[1] - y)
            if dist <= radius:
                if max_qual < qual:
                    max_qual = qual
                    min_coor = [x, y]
                elif max_qual == qual:
                    min_coor = min(min_coor, [x, y])

        return min_coor
