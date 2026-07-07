class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(row: int, col: int):
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0:
                #print("rejected", row, col)
                return 0
            #print(row, col)
            grid[row][col] = 0
            total = 1
            for x, y in directions:
                total += dfs(row + x, col + y)
            return total
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        #print(grid)
        return result

