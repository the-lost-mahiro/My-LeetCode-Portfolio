from collections import deque

class RideSharingSystem:

    def __init__(self):
        self.rQ = deque([])
        self.dQ = deque([])

    def addRider(self, riderId: int) -> None:
        self.rQ.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.dQ.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.rQ and self.dQ:
            r = self.rQ.popleft()
            d = self.dQ.popleft()
            return [d, r]
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rQ:
            self.rQ.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
