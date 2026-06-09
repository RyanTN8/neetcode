class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable = {}

        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            if s[i] not in hashTable:
                hashTable[s[i]] = 1
            else:
                hashTable[s[i]] += 1

            if t[i] not in hashTable:
                hashTable[t[i]] = -1
            else:
                hashTable[t[i]] -= 1
        
        for i in hashTable.values():
            if i != 0:
                return False
        return True
