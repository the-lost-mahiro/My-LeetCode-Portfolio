class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def cont(a):
            a.sort()
            max_cont = 1
            cur_cont = 1

            for i in range(1, len(a)):
                if a[i - 1] + 1 == a[i]:
                    cur_cont += 1
                else:
                    max_cont = max(max_cont, cur_cont)
                    cur_cont = 1
            
            return max(max_cont, cur_cont)
        
        return (min(cont(hBars), cont(vBars)) + 1) ** 2
