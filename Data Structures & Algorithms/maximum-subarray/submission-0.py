class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subArrayMax = float('-inf')
        globalMax = float('-inf')
        for i in range(len(nums)):
            if nums[i] > nums[i] + subArrayMax:
                subArrayMax = nums[i]
                globalMax = max(globalMax, subArrayMax)
            else:
                subArrayMax += nums[i]
                globalMax = max(globalMax, subArrayMax)
        return globalMax