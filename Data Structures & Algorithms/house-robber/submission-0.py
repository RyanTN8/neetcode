class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        profit = [0] * len(nums)
        profit[0], profit[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(profit)):
            profit[i] = max(profit[i - 2] + nums[i], profit[i - 1])
        
        return profit[-1]

