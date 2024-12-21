from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # * Solution using hashmap
        hashmap = {}
        # ? For every digit in nums, if the difference between the
        # ? Target and the current number is in the hashmap
        # ? That means there is a possible combo
        for count, currNum in enumerate(nums):
            diff = target - currNum
            if diff in hashmap:
                return [hashmap[diff], count]
            hashmap[currNum] = count
        # * Not needed for problem
        return list(hashmap)

        # * Brute Force Solution
        # for x in range(len(nums)):
        #     for y in range(x + 1, len(nums)):
        #         if (nums[x] + nums[y]) == target:
        #             return [x, y]
