class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        result = []

        for index, char in enumerate(s):
            if char in intervals:
                intervals[char][1] = index
            else:
                intervals[char] = [index, index]
        
        intervals = list(intervals.values())
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        for interval in intervals[1:]:
            if interval[0] > end:
                result.append(end - start + 1)
                start = interval[0]
                end = interval[1]
            else:
                end = max(end, interval[1])
                start = min(start, interval[0])
        result.append(end - start + 1)
        return result