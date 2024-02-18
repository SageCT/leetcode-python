from typing import Collection, List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = [(r, c)]
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if (
                        0 <= row + dr < rows
                        and 0 <= col + dc < cols
                        and grid[row + dr][col + dc] == "1"
                        and (row + dr, col + dc) not in visited
                    ):
                        q.append((row + dr, col + dc))
                        visited.add((row + dr, col + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands
