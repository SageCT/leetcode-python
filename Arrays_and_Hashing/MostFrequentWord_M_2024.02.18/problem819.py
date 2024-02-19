from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = (
            paragraph.lower()
            .replace(",", " ")
            .replace("!", " ")
            .replace("?", " ")
            .replace(";", " ")
            .replace(".", " ")
            .replace("'", " ")
            .replace(":", " ")
            .split()
        )
        return Counter([i for i in p if i not in banned]).most_common(1)[0][0]
