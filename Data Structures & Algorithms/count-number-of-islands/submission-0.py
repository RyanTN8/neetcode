class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int, grid: List[List[str]]) -> List[List[str]]:
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == "0":
                return grid
            grid[row][col] = "0"
            grid = dfs(row, col - 1, grid)
            grid = dfs(row - 1, col, grid)
            grid = dfs(row, col + 1, grid)
            grid = dfs(row + 1, col, grid)
            return grid
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid = dfs(i, j, grid)
        
        return count
                

