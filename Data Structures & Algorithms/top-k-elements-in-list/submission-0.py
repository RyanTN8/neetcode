class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = {}
        frequencies = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            if num not in hashTable:
                hashTable[num] = 1
                frequencies[1].append(num)
            else:
                frequencies[hashTable[num]].remove(num)
                hashTable[num] += 1
                frequencies[hashTable[num]].append(num)

        for i in range(len(frequencies) - 1, 0, -1):
            while frequencies[i]:
                result.append(frequencies[i][0])
                frequencies[i].pop(0)
            if len(result) == k:
                return result
