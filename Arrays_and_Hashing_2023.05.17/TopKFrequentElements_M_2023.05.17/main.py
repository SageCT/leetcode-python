import collections
import heapq
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)  # type: ignore
