import bisect
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [-1] * len(rains)
        full_lakes = {}
        dry_days = []
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1 
            else:
                if lake in full_lakes:
                    last_rain_day = full_lakes[lake]
                    idx = bisect.bisect_right(dry_days, last_rain_day)
                    if idx < len(dry_days):
                        day_to_dry = dry_days[idx]
                        ans[day_to_dry] = lake
                        dry_days.pop(idx)
                    else:
                        return []
                full_lakes[lake] = i
                
        return ans
