class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        start = intervals[0][0]
        end = intervals[0][1]
        result = []

        for interval in intervals[1:]:
            if interval[0] > end:
                result.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
                start = min(start, interval[0])
        result.append([start, end])
        return result