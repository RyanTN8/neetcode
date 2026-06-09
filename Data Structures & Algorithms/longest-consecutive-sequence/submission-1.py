class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = {}
        longest = 0

        for i, val in enumerate(nums):
            hashTable[val] = i

        for num in nums:
            curr = 0
            if num - 1 not in hashTable:
                temp = num
                while temp in hashTable:
                    temp += 1
                    curr += 1
            longest = max(longest, curr)
        return longest
