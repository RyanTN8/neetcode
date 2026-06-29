class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(index: int, subset: List[int]) -> None:
            if index == len(nums):
                nonlocal result
                result.append(subset[:])
                return
            
            subset.append(nums[index])
            backtrack(index + 1, subset)

            subset.pop(-1)
            backtrack(index + 1, subset)
        
        backtrack(0, [])
        return result
