class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        hashMap = {}
        for char in t:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        
        l = r = 0
        hashMapS = {}
        shortestLength = len(s) + 1
        shortestString = ""

        #loop until l and r are both at end

        #move right until all chars are covered
        #move left until window is no longer valid
        #save this substring and length
        #move left again

        while r < len(s) or all(hashMapS.get(char, 0) >= count for char, count in hashMap.items()):
            while r < len(s) and not all(hashMapS.get(char, 0) >= count for char, count in hashMap.items()):
                if s[r] in hashMapS:
                    hashMapS[s[r]] += 1
                else:
                    hashMapS[s[r]] = 1
                r = r + 1
            while l < len(s) and all(hashMapS.get(char, 0) >= count for char, count in hashMap.items()):
                if r - l <= shortestLength:
                    shortestLength = r - l
                    shortestString = s[l:r]
                hashMapS[s[l]] -= 1
                l = l + 1

        return shortestString
            

            

            

