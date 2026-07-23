class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dfs on any adjacent squares not visited and higher than or equal to current
        visitedP = set()
        visitedA = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(row: int, col: int, ocean: str) -> None:
            if ocean == 'P':
                visitedP.add((row, col))
            else:
                visitedA.add((row, col))

            for dx, dy in directions:
                x = row + dx
                y = col + dy

                if 0 <= x < ROWS and 0 <= y < COLS and heights[row][col] <= heights[x][y] and ((ocean == 'P' and (x, y) not in visitedP) or (ocean == 'A' and (x, y) not in visitedA)):
                    dfs(x, y, ocean)
        
        for i in range(COLS):

            dfs(0, i, 'P')
            dfs(ROWS - 1, i, 'A')
        
        for i in range(ROWS):
            dfs(i, 0, 'P')
            dfs(i, COLS - 1, 'A')

        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in visitedP and (i, j) in visitedA:
                    result.append([i, j])
        
        return result

        #run dfs on all of the edge ones depending if they're pacific or atlantic
        #return ones in both
