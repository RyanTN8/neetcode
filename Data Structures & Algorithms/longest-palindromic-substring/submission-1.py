class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l: int, r: int) -> str:
            nonlocal s
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        resultLen = 0
        result = ""

        for i in range(len(s)):
            l = check(i - 1, i)
            m = check(i, i)
            r = check(i, i + 1)

            if len(l) >= len(m) and len(l) >= len(r):
                if len(l) > resultLen:
                    resultLen = len(l)
                    result = l
            elif len(r) >= len(l) and len(r) >= len(m):
                if len(r) > resultLen:
                    resultLen = len(r)
                    result = r
            elif len(m) >= len(l) and len(m) >= len(r):
                if len(m) > resultLen:
                    resultLen = len(m)
                    result = m
        return result