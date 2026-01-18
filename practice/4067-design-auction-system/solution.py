class AuctionSystem:

    def __init__(self):
        self.itemBid = defaultdict(dict)
        self.itemHeap = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.itemBid[itemId][userId] = bidAmount
        heapq.heappush(self.itemHeap[itemId], (-bidAmount, -userId))
        
    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.itemBid[itemId][userId] = newAmount
        heapq.heappush(self.itemHeap[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.itemBid[itemId][userId]

        if not self.itemBid[itemId]:
            del self.itemBid[itemId]
            del self.itemHeap[itemId]

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.itemBid or not self.itemBid[itemId]:
            return -1

        heap = self.itemHeap[itemId]
        bids = self.itemBid[itemId]

        while heap:
            nBid, nUser = heap[0]
            user = -nUser
            bid = -nBid
            
            if user in bids and bids[user] == bid:
                return user

            heapq.heappop(heap)

        return -1

# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
