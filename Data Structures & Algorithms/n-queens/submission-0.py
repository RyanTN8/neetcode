class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def validSpot(row: int, col: int, board:List[str]) -> bool:
            #check row
            if 'Q' in board[row]:
                return False
            #check col
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            #check diagonal top-left
            r = row - 1
            c = col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            #check diagonal bot-right
            r = row + 1
            c = col + 1
            while r < n and c < n:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c += 1
            #check diagonal top-right
            r = row - 1
            c = col + 1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            #check diagonal bot-left
            r = row + 1
            c = col - 1
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
            return True

        result = []

        def backtrack(row: int, col: int, board:List[str]) -> None:
            #basecase - out of bounds
            if row >= n:
                for i in range(n):
                    if 'Q' not in board[i]:
                        return
                result.append(board.copy())
                return
            
            placed = False
            #case 1 - place a queen
            if validSpot(row, col, board):
                board[row] = board[row][:col] + 'Q' + board[row][col + 1:]
                if col == n - 1:
                    backtrack(row + 1, 0, board)
                else:
                    backtrack(row, col + 1, board)
                placed = True

            #case 2 - don't place a queen
            if placed:
                board[row] = board[row][:col] + "." + board[row][col + 1:]
            
            if col == n - 1:
                backtrack(row + 1, 0, board)
            else:
                backtrack(row, col + 1, board)
        
        boardRow = '.' * n
        b = ['.' * n for _ in range(n)]
        backtrack(0, 0, b)
        return result
            