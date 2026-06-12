class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            #for all cases
            if target == nums[m]:
                return m

            #no rotation
            if nums[l] < nums[r]:
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            #m, r in sorted
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            #l, m in sorted
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                print(l)
                print(r)
                print(m)
                print("fuck smth broke")
                break
            
        return -1
                
