from bisect import bisect_left
from itertools import combinations
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # ? N is half the number of elements in nums because
        # ? we are using the meet-in-the-middle technique
        N = len(nums) // 2
        summ = sum(nums)

        # get_sums to get all possible combinations of k elements
        # then puts them into a dictionary with key = k and value = list of sums
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
        half = (
            total // 2
        )  # the best sum required for each, we have to find sum nearest to this
        for k in range(1, N + 1):
            left = left_sums[k]
            right = right_sums[N - k]
            right.sort()
            for x in left:
                r = half - x  # ? find the sum nearest to half in right
                p = bisect_left(right, r)
                for q in [p, p - 1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        ans = min(ans, abs(left_ans_sum - right_ans_sum))
        return ans
