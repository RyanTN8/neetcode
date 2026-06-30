class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDistance = 0
        for i in range(len(nums)):
            if i > maxDistance:
                return False
            maxDistance = max(maxDistance, i + nums[i])
        return True
            