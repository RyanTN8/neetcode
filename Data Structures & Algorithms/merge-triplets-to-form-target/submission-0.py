class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False, False, False]
        for triplet in triplets:
            valid = True
            t = [False, False, False]
            for i in range(3):
                if triplet[i] > target[i]:
                    valid = False
                    break
                elif triplet[i] == target[i]:
                    t[i] = True
            if valid:
                for i in range(3):
                    good[i] = good[i] or t[i]
        return all(good)
        