from typing import List
import heapq

# * Brute Force
# class MedianFinder:
#     def __init__(self):
#         self.data = []

#     def addNum(self, num: int) -> None:
#         self.data.append(num)

#     def findMedian(self) -> float:
#         return float(sum(self.data) / len(self.data))


# * Neetcode Answer
class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be eual size
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # ? Because python doesn't have a native minheap
        # ? We have to use -1 when pushing and popping from the heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        return

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-1 * self.small[0])
        elif len(self.large) > len(self.small):
            return self.large[0]

        return float((-1 * (self.small[0]) + self.large[0]) / 2)
