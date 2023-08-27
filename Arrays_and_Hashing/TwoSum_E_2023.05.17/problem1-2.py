from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for count, currNum in enumerate(nums):
            diff = target - currNum
            if diff in hashmap:
                return [count, hashmap[diff]]
            hashmap[currNum] = count
