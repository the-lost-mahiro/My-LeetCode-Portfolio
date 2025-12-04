class Solution:
    def countCollisions(self, directions: str) -> int:
        stripped = directions.lstrip('L').rstrip('R')
                
        return len(stripped) - stripped.count('S')
