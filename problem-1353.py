from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        day = 0
        event_id = 0
        attended = 0
        n = len(events)
        
        while event_id < n or min_heap:
            if not min_heap:
                day = events[event_id][0]
            
            while event_id < n and events[event_id][0] <= day:
                heappush(min_heap, events[event_id][1])
                event_id += 1
            
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            
            if min_heap:
                heappop(min_heap)
                attended += 1
            
            day += 1
        
        return attended
