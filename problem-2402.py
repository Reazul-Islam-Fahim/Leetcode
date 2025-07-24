from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        busy_rooms = []
        room_usage = [0] * n

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room)

            duration = end - start

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room))
                room_usage[room] += 1
            else:
                soonest_end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(busy_rooms, (soonest_end_time + duration, room))
                room_usage[room] += 1

        max_meetings = max(room_usage)
        for i, count in enumerate(room_usage):
            if count == max_meetings:
                return i
