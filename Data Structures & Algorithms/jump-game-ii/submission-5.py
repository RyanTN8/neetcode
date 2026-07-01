class Solution:
    def jump(self, nums: List[int]) -> int:
        current = 0
        maxDistance = nums[0]
        jumps = 1

        if len(nums) == 1:
            return 0
            
        while maxDistance < len(nums) - 1:
            for i in range(current, maxDistance + 1):
                if i + nums[i] > maxDistance:
                    current = i
                    maxDistance = i + nums[i]
            jumps += 1
        return jumps