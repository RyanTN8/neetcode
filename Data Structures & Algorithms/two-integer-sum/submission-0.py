class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            hashMap[num] = i

        for i, num in enumerate(nums):
            if target - num in hashMap and hashMap[target - num] != i:
                return [i, hashMap[target - num]]
        
        return []