from bisect import bisect_left
from itertools import combinations
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # ? N is half the number of elements in nums because
        # ? we are using the meet-in-the-middle technique
        N = len(nums) // 2

        # ? get_sums to get all possible combinations of k elements
        # ? then puts them into a dictionary with key = k and value = list of sums
        def get_sums(nums) -> dict[int, List[int]]:
            ans = {}
            N = len(nums)
            for k in range(1, N + 1):
                sums = []
                for comb in combinations(nums, k):
                    sums.append(sum(comb))
                ans[k] = sums
            return ans

        # ? divide the array into two parts, left and right
        left_part, right_part = nums[:N], nums[N:]
        left_sums, right_sums = get_sums(left_part), get_sums(right_part)

        ans = abs(sum(left_part) - sum(right_part))
        total = sum(nums)
        # ? the best sum required for each, we have to find sum nearest to this
        half = total // 2

        # ? we start at 0 to avoid the case where we would take 0 elements from left
        # ! This is the meet-in-the-middle technique
        for k in range(1, N + 1):
            # ? Left is a list of each possible combination of left_part
            left = left_sums[k]
            right = right_sums[N - k]
            right.sort()  # We sort right to use bisect_left()
            # * From here we do the process of elmimination
            # * We find the sum nearest to half in right AND TEST for each sum in left
            for x in left:
                sumNearest = half - x  # ? find the sum nearest to half in right
                p = bisect_left(right, sumNearest)
                # ! Essentially,
                for q in [p, p - 1]:
                    if 0 <= q < len(right):
                        # ? Left selection + right selection
                        left_ans_sum = x + right[q]
                        # ? Possible right selection based off left over from above left selection
                        right_ans_sum = total - left_ans_sum
                        # ? Check if ans is smaller than current ans!
                        ans = min(ans, abs(left_ans_sum - right_ans_sum))
        return ans


nums1 = [1, 6, 11, 5]
nums2 = [3, 9, 7, 3]
print(Solution().minimumDifference(nums2))
