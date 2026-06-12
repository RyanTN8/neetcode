import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #1. add each value to the maxHeap with the index
        #2. while peek(maxHeap) is the maximum, delete the first value in the heap
        print(nums)
        result = [-10001] * (len(nums) - k + 1)
        heap = []
        for i in range(k - 1):
            heapq.heappush_max(heap, (nums[i], i))
        #pop -> largest = heapq.heappop_max(data)
        #push -> heapq.heappush_max(my_max_heap, 25)
        #peek -> largest = my_max_heap[0]

        for i in range(len(nums) - k + 1):
            heapq.heappush_max(heap, (nums[i + k - 1], i + k - 1))
            while heap[0][1] not in range(i, i + k):
                heapq.heappop_max(heap)
            result[i] = heap[0][0]
        return result

