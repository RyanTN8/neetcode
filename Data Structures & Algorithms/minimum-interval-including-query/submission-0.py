import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort intervals by start value
        #process queries in ascending order
        #   add intervals to min-heap while their start values are <= query, store end values and size
        #   min-heap ordered by interval size. remove elements while their end is < query

        intervals.sort(key = lambda x: x[0])
        queries = [(queries[i], i ) for i in range(len(queries))]
        queries.sort(key = lambda x: x[0])
        i = 0 #for intervals
        heap = []
        result = [-1] * len(queries)

        for query in queries:
            while i < len(intervals) and intervals[i][0] <= query[0]:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while heap and heap[0][2] < query[0]:
                heapq.heappop(heap)
            if heap:
                result[query[1]] = heap[0][0]
        return result




