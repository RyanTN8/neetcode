class PrefixTree:

    def __init__(self):
        self.letters = {}

    def insert(self, word: str) -> None:
        curr = self.letters

        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        curr['X'] = 0

    def search(self, word: str) -> bool:
        curr = self.letters
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return 'X' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.letters
        for char in prefix:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return True
        