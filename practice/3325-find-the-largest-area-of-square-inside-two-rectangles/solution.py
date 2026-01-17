class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_side = 0

        for (bli, tri), (blj, trj) in combinations(zip(bottomLeft, topRight), 2):
            w = min(tri[0], trj[0]) - max(bli[0], blj[0])
            h = min(tri[1], trj[1]) - max(bli[1], blj[1])

            max_side = max(max_side, min(w, h))

        return max_side * max_side
