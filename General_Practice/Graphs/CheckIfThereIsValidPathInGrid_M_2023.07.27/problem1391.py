from typing import List
from collections import deque


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        up = {x: set([2, 3, 4]) for x in [2, 5, 6]}
        down = {x: set([2, 5, 6]) for x in [2, 3, 4]}
        left = {x: set([1, 4, 6]) for x in [1, 3, 5]}
        right = {x: set([1, 3, 5]) for x in [1, 4, 6]}
        grid[0][0] = -grid[0][0]

        queue = deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            # ? If we have reached the bottom left position, (i last row, j last column)
            # ? We have completed the bfs
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True

            # ? We can go up, down, left, or right. Traverse each direction.
            # ! k, l are the current row and col. i and j are the next col and row.
            for k, l, d in [
                (i - 1, j, up),
                (i + 1, j, down),
                (i, j - 1, left),
                (i, j + 1, right),
            ]:
                # ? because we preemptively switch visited to neg (see line 11)
                # ? we check to see if the current node was visited (-grid[i][j] in d)
                # ? we also check if the node direction is in the directions of the visited node
                # ? (grid[k][l] in d[-grid[i][j]])
                if (
                    0 <= k < len(grid)
                    and 0 <= l < len(grid[0])
                    and -grid[i][j] in d
                    and grid[k][l] in d[-grid[i][j]]
                ):
                    grid[k][l] = -grid[k][l]
                    queue.append((k, l))
        return False
