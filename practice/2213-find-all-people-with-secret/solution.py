from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret = {0, firstPerson}
        meetings.sort(key = lambda x: (x[2]))

        a = len(meetings)
        i = 0

        while i < a:
            graph = defaultdict(list)
            time = meetings[i][2]
            people = set()

            while i < a and meetings[i][2] == time:
                p1, p2 = meetings[i][0], meetings[i][1]
                graph[p1].append(p2)
                graph[p2].append(p1)
                people.add(p1)
                people.add(p2)
                i += 1
            
            queue = deque([p for p in people if p in secret])

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in secret:
                        secret.add(neighbor)
                        queue.append(neighbor)

        return list(secret)
