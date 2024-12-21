from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Char is going to be the last index in s.
        hash_map = {}
        for i, c in enumerate(s):
            hash_map[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, hash_map[c])
            if i == end:
                res.append(size)
                size = 0
        return res
