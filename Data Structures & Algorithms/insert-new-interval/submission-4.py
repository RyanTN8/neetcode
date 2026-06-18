class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #iterate through all the intervals
        #store the first and last intervals overlapping and their index
        #combine those intervals
        startIndex = newInterval[0]
        endIndex = newInterval[1]

        result = []
        for interval in intervals:
            if newInterval[0] <= interval[0] <= newInterval[1] or newInterval[0] <= interval[1] <= newInterval[1] or interval[0] <= newInterval[0] < newInterval[1] <= interval[1]:
                startIndex = min(interval[0], startIndex)
                endIndex = max(interval[1], endIndex)
            else:
                result.append(interval)

        for i in range(len(result)):
            if startIndex < result[i][1]:
                result.insert(i, [startIndex, endIndex])
                return result
        result.append([startIndex, endIndex])
        return result