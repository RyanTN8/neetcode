class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i: int, subset: List[int]) -> None:
            if sum(subset) == target:
                result.append(subset[:])
                return
            elif i >= len(nums) or sum(subset) > target:
                return

            #use current number, dont move on
            subset.append(nums[i])
            backtrack(i, subset)
            #skip current number
            subset.pop(-1)
            backtrack(i + 1, subset)
        backtrack(0, [])
        return result   

        # def backtrack(index: int, subset: List[int]) -> None:
        #     if index == len(nums):
        #         result.append(subset[:])
        #         return
            
        #     subset.append(nums[index])
        #     backtrack(index + 1, subset)

        #     subset.pop(-1)
        #     backtrack(index + 1, subset)
        
        # backtrack(0, [])
        # return result

