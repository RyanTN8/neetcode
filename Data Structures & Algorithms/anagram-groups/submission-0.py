class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        result = []
        #ord('x') - ord('a') = index

        for string in strs:
            arr = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                arr[index] += 1
            if tuple(arr) not in hashMap:
                hashMap[tuple(arr)] = []
            hashMap[tuple(arr)].append(string)

        
        for key in hashMap.keys():
            result.append(hashMap[key])
        
        return result