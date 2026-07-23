class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #iterate through board
        #if 'O' and not in grouping, run dfs and add all connected elements to grouping
        #go through groupings check if any of them are edges and delete that whole grouping from list of groupings
        #rewrite board with new groupings

        hashMap = {}
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        groupings = []

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row: int, col: int, prev: (int, int)) -> None:
            if (row, col) in hashMap:
                return
            
            if prev == (-1, -1):
                hashMap[(row, col)] = len(groupings)
                groupings.append([(row, col)])
            else:
                index = hashMap[prev]
                hashMap[(row, col)] = index
                groupings[index].append((row, col))
            
            for dx, dy in directions:
                x = row + dx
                y = col + dy
                if 0 <= x < ROWS and 0 <= y < COLS and (x, y) not in hashMap and board[x][y] == 'O':
                    dfs(x, y, (row, col))
            
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    dfs(i, j, (-1, -1))

        result = []

        for group in groupings:
            for x, y in group:
                if x == 0 or x == ROWS - 1 or y == 0 or y == COLS - 1:
                    result.extend(group)
                    break
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in result:
                    board[i][j] = 'X'
            



            



            