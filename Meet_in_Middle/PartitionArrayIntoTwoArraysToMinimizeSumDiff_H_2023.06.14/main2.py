from typing import List


# Thought process:
# We can use a divide and conquer approach to solve this problem.
# We can divide the array into two parts, left and right.
# Then solve using a recursive funciton.
# ! Does not work if the array is equal i.e. [-x, x]


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # The Recursive function that finds the minimum difference
        def findMinRec(
            n: List[int], i: int = 0, sumCalculated: int = 0, sumTotal: int = 0
        ) -> int:
            # ? Base Case
            # If we have reached the end of the array, we return the absolute difference between the sum of the left and right parts
            if i == -1:
                return abs((sumTotal - sumCalculated) - sumCalculated)

            # Returns the minimum of the two cases:
            return min(
                findMinRec(n, i - 1, sumCalculated + n[i - 1], sumTotal),
                findMinRec(n, i - 1, sumCalculated, sumTotal),
            )

        nums.sort()

        return findMinRec(nums, len(nums), 0, sum(nums))


test1 = [3, 9, 7, 3]
test2 = [-36, 36]

print(Solution().minimumDifference(test1))
