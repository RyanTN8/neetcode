"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        start = end = 0
        count = result = 0

        while start < len(intervals):
            if starts[start] < ends[end]:
                start += 1
                count += 1
            else:
                end += 1
                count -= 1
            result = max(result, count)
        return result