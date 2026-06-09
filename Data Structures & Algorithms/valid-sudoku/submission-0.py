class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        def getSquare(row: int, col: int) -> int:
            row //= 3
            col //= 3
            
            if row == 0 and col == 0:
                return 0
            elif row == 1 and col == 0:
                return 1    
            elif row == 2 and col == 0:
                return 2
            elif row == 0 and col == 1:
                return 3
            elif row == 1 and col == 1:
                return 4    
            elif row == 2 and col == 1:
                return 5
            elif row == 0 and col == 2:
                return 6
            elif row == 1 and col == 2:
                return 7    
            elif row == 2 and col == 2:
                return 8



        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[getSquare(row,col)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[getSquare(row,col)].add(board[row][col])
        return True


    








