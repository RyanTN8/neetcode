import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heapq.heapify(hand)

        result = []

        while hand:
            card = hand[0]
            if not result:
                result.append([heapq.heappop(hand)])
            else:
                added = False
                for i in range(len(result)):
                    if len(result[i]) == groupSize:
                        continue
                    if card == result[i][-1] + 1:
                        result[i].append(heapq.heappop(hand))
                        added = True
                        break
                if not added:
                    result.append([heapq.heappop(hand)])
        print(result)
        for i in range(len(result)):
            if len(result[i]) != groupSize:
                return False
        return True