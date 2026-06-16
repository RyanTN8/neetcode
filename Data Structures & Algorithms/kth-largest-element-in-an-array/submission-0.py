import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush_max(heap, num)
        for i in range(k - 1):
            heapq.heappop_max(heap)
        return heapq.heappop_max(heap)