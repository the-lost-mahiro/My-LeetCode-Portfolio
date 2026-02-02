from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        m = k - 1
        
        sl = SortedList(nums[1 : dist + 2])
        current_sum = sum(sl[:m])
        ans = current_sum

        for i in range(1, n):

            old_val = nums[i]
            idx = sl.bisect_left(old_val)
            
            if idx < m:
                current_sum -= old_val

                if len(sl) > m:
                    current_sum += sl[m]
            sl.remove(old_val)

            new_idx = i + dist + 1
            if new_idx < n:
                new_val = nums[new_idx]
                sl.add(new_val)
                pos = sl.bisect_left(new_val)

                if pos < m:
                    current_sum += new_val

                    if len(sl) > m:
                        current_sum -= sl[m]

            if len(sl) >= m:
                ans = min(ans, current_sum)

            if i + dist + 1 >= n and len(sl) <= m:
                break
                
        return nums[0] + ans
