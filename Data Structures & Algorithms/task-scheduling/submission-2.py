import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #get frequencies of each letter -> store in hash map
        #make max heap with (freq, char)
        #iterate through the max heap, process the letter if it can be processes, else use the next available one

        hashMap = {}
        heap = []
        result = []

        for task in tasks:
            hashMap[task] = hashMap.get(task, 0) + 1
        
        for key in hashMap:
            heapq.heappush_max(heap, (hashMap[key], key))

        # # Find the 2nd largest element (n = 2)
        # n = 2
        # nth_largest = heapq.nlargest(n, heap)[-1]
        while heap:
            processed = False
            for i in range(1, len(heap) + 1):
                candidate = heapq.nlargest(i, heap)[-1]
                ithLargest = candidate[1]
                
                #check last n elements, see if ithLargest is in there
                subarr = result[max(0, len(result) - n):]
                if ithLargest not in subarr:
                    result.append(ithLargest)
                    #k, v = heapq.heappop_max(heap)
                    heap.remove(candidate)
                    heapq.heapify(heap)
                    if candidate[0] > 1:
                        heapq.heappush_max(heap, (candidate[0] - 1, ithLargest))
                    processed = True
                    break
            if not processed:
                result.append("/")
        return len(result)

        

