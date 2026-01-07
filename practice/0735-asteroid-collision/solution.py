class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                r = 0
                while stack and stack[-1] > 0:
                    r = stack.pop()

                    if r + a < 0:
                        continue

                    elif r + a == 0:
                        break

                    else:
                        stack.append(r)
                        break
                
                if r + a < 0:
                    stack.append(a)
            
            else:
                stack.append(a)
        
        return stack
