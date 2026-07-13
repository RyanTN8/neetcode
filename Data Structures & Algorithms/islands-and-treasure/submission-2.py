class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(row: int, col: int) -> None:
        #run bfs on the cell and label all available cells by the distance to it
            queue = []
            queue.append((row, col, 0))
            visited = []

            while queue:
                r, c, d = queue.pop()

                #if tile is water or out of bounds or tile visited, continue
                if 0 > r or r >= ROWS or 0 > c or c >= COLS or grid[r][c] == -1 or ((r, c) in visited and d > grid[r][c]):
                    continue

                #process current tile
                grid[r][c] = min(grid[r][c], d)
                visited.append((r, c))

                for x, y in directions:
                    queue.append((r + x, c + y, d + 1))
                
        #for loop iterating through all cells, if cell is 0, run bfs on it
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j)