class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        state = [0] * numCourses
        result = []

        def has_cycle(u):
            if state[u] == 1:
                return True

            if state[u] == 2:
                return False
            
            state[u] = 1
            
            for v in adj[u]:
                if has_cycle(v):
                    return True
            
            state[u] = 2
            result.append(u)
            return False

        for i in range(numCourses):
            if state[i] == 0:
                if has_cycle(i):
                    return []
        
        return result[::-1]
