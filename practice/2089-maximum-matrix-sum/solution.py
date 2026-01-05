import heapq

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        zero = False
        neg_hp = []
        pos_hp = []

        heapq.heapify(neg_hp)
        heapq.heapify(pos_hp)

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                cur = matrix[i][j]
                if cur == 0:
                    zero = True
                    
                elif cur > 0:
                    heapq.heappush(pos_hp, cur)

                else:
                    heapq.heappush(neg_hp, - cur)
        fix_sum = sum(pos_hp) + sum(neg_hp)
        if zero or len(neg_hp) % 2 == 0:
            return fix_sum

        else:
            if not pos_hp:
                return fix_sum - 2 * neg_hp[0]
            if not neg_hp:
                return fix_sum
                
            if pos_hp[0] < neg_hp[0]:
                return fix_sum - 2 * pos_hp[0]

            else:
                return fix_sum - 2 * neg_hp[0]
