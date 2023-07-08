from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row by adding them to a set
        for x in range(3):
            bigRowCheck: List[str] = []
            for y in range(3):
                for i in range(3):
                    for j in range(3):
                        tempCheck.add(board[i][j])

        for row in board:
            if not self.is_valid(row):
                return False

        for y in range(len(board)):
            unit: List[str] = []
            for x in range(len(board[y])):
                unit.append(board[y][x])

    def is_valid(self, unit: List[str]) -> bool:
        unit = [x for x in unit if x != "."]
        return len(set(unit)) == len(unit)
