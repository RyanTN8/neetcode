class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #put all unique characters of string into set
        #iterate through charSet and figure out longest substring with k replacements
        #return the max
        result = 0
        charSet = set(s)

        for char in charSet:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                
                result = max(result, r - l + 1)
        return result


