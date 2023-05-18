import collections
import heapq
from typing import List
from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         print(count)
#         toReturn = []

#         for i in count.most_common(k):
#             toReturn.append(i[0])

#         return toReturn

#     import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = collections.Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)
