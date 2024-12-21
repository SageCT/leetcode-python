from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        toReplace = []

        for i in range(len(intervals)):
            # ? If the max of the new interval is less than the
            # ? beginning of the current one, we have found where it goes
            if newInterval[1] < intervals[i][0]:
                toReplace.append(newInterval)
                return toReplace + intervals[i:]
            # ? If the min of the current interval is greater than the max
            # ? of the current interval, we have found where it goes
            elif newInterval[0] > intervals[i][1]:
                toReplace.append(intervals[i])

            # ? If there is an overlap, then we get the min and max of
            # ? the current interval and compare them with the new interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        toReplace.append(newInterval)
        return toReplace


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]


print(Solution().insert(intervals, newInterval))
