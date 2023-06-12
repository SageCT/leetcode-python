from typing import List
import numpy as np


# * Remember that this is a two pointer problem,
# * chances are you start at opposite ends of the list and iterate towards each other
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) // 2):
                for k in range(j + 1, len(nums)):
                    if (
                        nums[i] + nums[j] + nums[k] == 0
                        and sorted([nums[i], nums[j], nums[k]]) not in ans
                    ):
                        ans.append(sorted([nums[i], nums[j], nums[k]]))

        # ans = np.unique(ans).tolist()
        return ans
