class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        valid = []
        n = len(words)
        
        def backtrack(path):
            if len(path) == 4:
                valid.append(path[:])
                return

            for i in range(n):
                if words[i] not in path:
                    if len(path) == 0:
                        path.append(words[i])
                        backtrack(path)
                        path.pop()
    
                    elif len(path) == 1 and path[0][0] == words[i][0]:
                        path.append(words[i])
                        backtrack(path)
                        path.pop()
    
                    elif len(path) == 2 and path[0][3] == words[i][0]:
                        path.append(words[i])
                        backtrack(path)
                        path.pop()
    
                    elif len(path) == 3 and path[1][3] == words[i][0] and path[2][3] == words[i][3]:
                        path.append(words[i])
                        backtrack(path)
                        path.pop()

        backtrack([])

        valid.sort()
        
        return valid
