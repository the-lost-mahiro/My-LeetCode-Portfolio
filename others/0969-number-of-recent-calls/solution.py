from collections import deque

class RecentCounter:

    def __init__(self):
        self.values = deque()

    def ping(self, t: int) -> int:
        self.values.append(t)

        while self.values[0] < t - 3000:
            self.values.popleft()
        
        return len(self.values)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
