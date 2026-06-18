"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort intervals by end time
        sortedIntervals = sorted(intervals, key = lambda x: x.end)
        if not intervals:
            return True
        end = sortedIntervals[0].end
        for i in range(1, len(sortedIntervals)):
            nextStart = sortedIntervals[i].start
            if nextStart < end:
                return False
            end = sortedIntervals[i].end
        return True

