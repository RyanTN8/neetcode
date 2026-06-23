import heapq

class MedianFinder:

    def __init__(self):
        self.top = [100001] #minHeap
        self.bot = [-100001] #maxHeap

    def addNum(self, num: int) -> None:
        if self.bot[0] < num < self.top[0]: # num between two middle values
            if len(self.bot) <= len(self.top):
                heapq.heappush_max(self.bot, num)
            else:
                heapq.heappush(self.top, num)
        elif num <= self.bot[0]: # num falls under bot
            heapq.heappush_max(self.bot, num)
            if len(self.bot) > len(self.top) + 1:
                val = heapq.heappop_max(self.bot)
                heapq.heappush(self.top, val)
        else: #num falls under top
            heapq.heappush(self.top, num)
            if len(self.top) > len(self.bot) + 1:
                val = heapq.heappop(self.top)
                heapq.heappush_max(self.bot, val)


    def findMedian(self) -> float:
        #if no elms added
        if len(self.bot) == 1 and len(self.top) == 1:
            return -1
        #even number of elms
        if (len(self.bot) + len(self.top)) % 2 == 0:
            return (self.bot[0] + self.top[0]) / 2
        #odd number of elms
        #bot is bigger
        if len(self.bot) > len(self.top):
            return float(self.bot[0])
        #top is bigger
        else:
            return float(self.top[0])
        