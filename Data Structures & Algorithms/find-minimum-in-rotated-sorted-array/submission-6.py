class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            #l, mid are in same section -> break in right
            if nums[mid] > nums[r]:
                l = mid + 1
            #r, mid in same section -> break in left
            elif nums[l] > nums[mid]:
                r = mid
        return nums[l]
