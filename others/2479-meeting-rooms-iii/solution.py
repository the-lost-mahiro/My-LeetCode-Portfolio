import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)

        used_rooms = []
        heapq.heapify(used_rooms)

        count = [0] * n
        for start, end in meetings:

            while used_rooms and used_rooms[0][0] <= start:
                time_end, room_id = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room_id)

            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                count[room_id] += 1
                heapq.heappush(used_rooms, [end, room_id])
            
            else:
                earliest_end, room_id = heapq.heappop(used_rooms)
                count[room_id] += 1

                new_end = earliest_end + (end - start)
                heapq.heappush(used_rooms, [new_end, room_id])
        
        max_usage = max(count)
        for i in range(n):
            if count[i] == max_usage:
                return i
