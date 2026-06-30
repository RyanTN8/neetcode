class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True
            if (row < 0 or col < 0 or row >= rows or col >= cols):
                return False
            if word[i] != board[row][col] or visited[row][col]:
                return False

            visited[row][col] = True

            u = backtrack(row - 1, col, i + 1)
            d = backtrack(row + 1, col, i + 1)
            l = backtrack(row, col - 1, i + 1)
            r = backtrack(row, col + 1, i + 1)

            visited[row][col] = False
            return u or d or l or r

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


