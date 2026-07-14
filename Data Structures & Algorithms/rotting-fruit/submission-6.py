from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        distances = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()
        visited = set()
        distance = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                distances[r][c] = distance

                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < ROWS and 0 <= y < COLS and (x, y) not in visited and grid[x][y] != 0:
                        queue.append((x, y))
                        visited.add((x, y))
            distance += 1

        minMinutes = -1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and distances[i][j] == 0:
                    return -1
                minMinutes = max(minMinutes, distances[i][j])
        return minMinutes
                
                
