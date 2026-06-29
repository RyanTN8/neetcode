class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # add the words in the trie
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['.'] = '.'
        
        result = []

        def helper(x: int, y: int, board: List[List[str]], trie: dict, word: str) -> None:
            if board[y][x] not in trie:
                return

            word += (board[y][x])
            trie = trie[board[y][x]]

            nonlocal result
            if '.' in trie and word not in result:
                result.append(word)
                

            new_board = [r[:] for r in board]  # deep copy
            new_board[y][x] = '-'
            
            if x > 0:
                helper(x - 1, y, new_board, trie, word)
            if x < len(board[0]) - 1:
                helper(x + 1, y, new_board, trie, word)
            if y > 0:
                helper(x, y - 1, new_board, trie, word)
            if y < len(board) - 1:
                helper(x, y + 1, new_board, trie, word)


        for i in range(len(board)):
            for j in range(len(board[0])):
                helper(j, i, board, trie, "")
        
        return result