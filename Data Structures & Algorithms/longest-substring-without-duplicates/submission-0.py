class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        maxLength = 0

        for i in range(len(s)):
            while s[i] in charSet:
                #move left pointer
                charSet.remove(s[left])
                left += 1

            
            charSet.add(s[i])
            maxLength = max(maxLength, i - left + 1)

        return maxLength