class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [1] * len(nums)
        suffixProduct = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
            suffixProduct[-i-1] = suffixProduct[-i] * nums[-i]

        print(prefixProduct)
        print(suffixProduct)

        result = []
        for i in range(len(nums)):
            result.append(prefixProduct[i] * suffixProduct[i])
        
        return result
