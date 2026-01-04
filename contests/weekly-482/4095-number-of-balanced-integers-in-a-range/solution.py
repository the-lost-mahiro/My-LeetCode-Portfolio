from functools import lru_cache

class Solution:
    def countBalanced(self, low: int, high: int) -> int:

        def solve(n: int) -> int:
            if n < 0: return 0
            s = str(n)
            
            @lru_cache(None)
            def dp(idx, diff, is_limit, is_started, is_odd_pos):
                if idx == len(s):
                    return 1 if is_started and diff == 0 else 0
                
                res = 0
                upper = int(s[idx]) if is_limit else 9
                
                for d in range(upper + 1):
                    new_limit = is_limit and (d == upper)
                    
                    if not is_started:
                        if d == 0:
                            res += dp(idx + 1, 0, new_limit, False, True)
                        else:
                            res += dp(idx + 1, d, new_limit, True, False)
                    else:
                        new_diff = diff + d if is_odd_pos else diff - d
                        res += dp(idx + 1, new_diff, new_limit, True, not is_odd_pos)
                return res

            total_balanced = dp(0, 0, True, False, True)

            single_digit_balanced = 0
            for i in range(min(n, 9) + 1):
                pass 

            return total_balanced

        ans_high = solve(high)
        ans_low = solve(low - 1)

        return (ans_high - ans_low)
        
