class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + '|' + word
        return result


    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            length = ""
            print(length)
            word = ""
            while s[i] != '|':
                length += s[i]
                i += 1
            i += 1
            length = int(length)
            for j in range(length):
                word += s[i]
                i += 1
            words.append(word)
        return words

