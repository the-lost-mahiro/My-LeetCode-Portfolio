class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total_sum = sum(batteries)
        
        while batteries:
            big_battery = batteries[-1]
            avg = total_sum // n
            if big_battery > avg:
                total_sum -= batteries.pop()
                n -= 1
            else:
                return avg    
        return 0
