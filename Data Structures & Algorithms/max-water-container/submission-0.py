class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #greedy: move the smaller of the two pillars
        l = 0
        r = len(heights) - 1
        maxWater = (r - l) * min(heights[l], heights[r])

        while l < r:
            maxWater = max(maxWater, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater