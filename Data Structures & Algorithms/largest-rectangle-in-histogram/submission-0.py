class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #make prefix and suffix lists for the next height < curr
        #calculate max area by height * distance between prefix and suffix
        length = len(heights)
        prefix = [-1] * length
        suffix = [-1] * length
        stack = []

        #create suffix and prefix next num < num with monotonic stack
        #prefix
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                prefix[stack[-1]] = i - stack[-1] - 1
                stack.pop(-1)
            stack.append(i)
        
        #suffix
        for i in range(length - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                suffix[stack[-1]] = stack[-1] - i - 1
                stack.pop(-1)
            stack.append(i)
        
        #post process -1s
        for i in range(length):
            if prefix[i] == -1:
                prefix[i] = length - i - 1
            if suffix[i] == -1:
                suffix[i] = i

        maxHeight = -1
        for i in range(length):
            height = heights[i]
            length = prefix[i] + 1 + suffix[i]
            maxHeight = max(maxHeight, height * length)
        
        return maxHeight

