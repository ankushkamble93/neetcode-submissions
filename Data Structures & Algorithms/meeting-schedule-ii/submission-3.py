"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        heapq.heappush(min_heap, intervals[0].end)
        for meetings in intervals[1:]:
            curr_start = meetings.start
            curr_end = meetings.end
            if min_heap and min_heap[0] <= curr_start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, curr_end)
        return len(min_heap)