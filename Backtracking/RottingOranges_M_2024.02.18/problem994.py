from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    if (
                        0 <= row + dr < rows
                        and 0 <= col + dc < cols
                        and grid[row + dr][col + dc] == 1
                    ):
                        fresh -= 1
                        grid[row + dr][col + dc] = 2
                        q.append((row + dr, col + dc))
            time += 1
        return time if fresh == 0 else -1
