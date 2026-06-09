class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = []
        suffixMax = [0] * len(height)
        pMax = 0
        sMax = 0
        result = [0] * len(height)

        for i in range(len(height)):
            #prefix
            prefixMax.append(pMax)
            pMax = max(pMax, height[i])
            #suffix
            suffixMax[-i-1] = sMax
            sMax = max(sMax, height[-i-1])

        for i in range(len(height)):
            result[i] = max(0, min(prefixMax[i], suffixMax[i]) - height[i])
        
        return sum(result)