class WordDictionary:

    def __init__(self):
        self.letters = {}

    def addWord(self, word: str) -> None:
        curr = self.letters

        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        curr['X'] = 0

    def search(self, word: str) -> bool:
        def searchDot(word: str, curr: dict) -> bool:
            if len(word) == 0:
                if 'X' in curr:
                    return True
                else:
                    return False
            
            char = word[0]
            if char == '.':
                flag = False
                for d in curr.values():
                    if d != 0 and searchDot(word[1:], d):
                        flag = True
                return flag
            else:
                if char in curr:
                    return searchDot(word[1:], curr[char])
                return False
        return searchDot(word, self.letters)
                
        