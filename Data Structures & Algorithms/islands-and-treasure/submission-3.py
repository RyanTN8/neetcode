from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        d = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = d

                # #if tile is water or out of bounds or tile visited, continue
                # if 0 > r or r >= ROWS or 0 > c or c >= COLS or grid[r][c] == -1 or ((r, c) in visited and d > grid[r][c]):
                #     continue

                # #process current tile
                # grid[r][c] = min(grid[r][c], d)
                # visited.append((r, c))

                for x, y in directions:
                    if 0 <= r + x < ROWS and 0 <= c + y < COLS and (r + x, c + y) not in visited and grid[r + x][c + y] != -1:
                        queue.append((r + x, c + y))
                        visited.add((r + x, c + y))
            
            d += 1