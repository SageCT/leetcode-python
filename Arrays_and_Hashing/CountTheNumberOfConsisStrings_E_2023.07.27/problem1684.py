from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in words:
            if set(i).issubset(set(allowed)):
                ans += 1

        return ans
