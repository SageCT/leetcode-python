from typing import List
from collections import Counter


class Solution:
    def countPairs(self, yum: List[int]) -> int:
        counts = Counter()
        MOD = 10**9 + 7

        total = 0
        for x in yum:
            for y in range(22):
                target = (1 << y) - x

                if target in counts:
                    total += counts[target]
            counts[x] += 1
        return total % MOD
