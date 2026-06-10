class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #for each element, mark that index as negative (abs -> * -1 -> ensures negative stay negative)
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            nums[abs(nums[i])] *= -1
        return