class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(l: int, r: int) -> str:
            nonlocal s
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        substrings = 0

        for i in range(len(s)):
            substrings += check(i - 1, i) + check(i, i)
        return substrings