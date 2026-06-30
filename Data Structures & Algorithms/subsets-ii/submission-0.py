class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i: int, subset: List[int]) -> None:
            if i == len(nums):
                result.append(subset.copy())
                return
            
            #case 1: take nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            subset.pop()

            #case 2: dont take nums[i], also prevent reputting the one just popped
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return result
