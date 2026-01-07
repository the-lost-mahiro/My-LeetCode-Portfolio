from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        r_count = senate.count('R')
        d_count = senate.count('D')
        
        r_ban_debt = 0
        d_ban_debt = 0
        
        while r_count > 0 and d_count > 0:
            current = queue.popleft()
            
            if current == 'R':
                if r_ban_debt > 0:
                    r_ban_debt -= 1
                    r_count -= 1

                else:
                    d_ban_debt += 1
                    queue.append('R')
                    
            else:
                if d_ban_debt > 0:
                    d_ban_debt -= 1
                    d_count -= 1

                else:
                    r_ban_debt += 1
                    queue.append('D')
                    
        return "Radiant" if r_count > 0 else "Dire"
