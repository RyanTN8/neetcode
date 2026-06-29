class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(subset: List[int], remainingNums: List[int]):
            #base case
            if len(subset) == len(nums):
                result.append(subset.copy())
            
            #choose one out of the remaining nums
            for i in range(len(remainingNums)):
                subset.append(remainingNums[i])
                backtrack(subset, remainingNums[:i] + remainingNums[i + 1:])
                subset.pop()
        backtrack([], nums)
        return result