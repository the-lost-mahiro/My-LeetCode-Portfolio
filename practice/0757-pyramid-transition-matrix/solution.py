class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mapping = defaultdict(list)
        for a, b, c in allowed:
            mapping[a + b].append(c)
            
        memo = {}

        def solve(current_row, next_row):
            state = (current_row, next_row)
            if state in memo:
                return memo[state]
            
            if len(current_row) == 1:
                return True
            
            if len(next_row) == len(current_row) - 1:
                res = solve(next_row, "")
                memo[state] = res
                return res
            
            i = len(next_row)
            pair = current_row[i : i + 2]
            
            for char in mapping[pair]:
                if solve(current_row, next_row + char):
                    memo[state] = True
                    return True
            
            memo[state] = False
            return False

        return solve(bottom, "")
