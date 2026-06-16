import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush_max(heap, stone)

        while len(heap) > 1:
            bigRock = heapq.heappop_max(heap)
            littleRock = heapq.heappop_max(heap)

            if bigRock != littleRock:
                heapq.heappush_max(heap, bigRock - littleRock)
        
        if heap:
            return heap[0]
        return 0

