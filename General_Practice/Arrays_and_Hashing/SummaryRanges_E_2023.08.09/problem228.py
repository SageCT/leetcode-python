from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        curr = (nums[0], -232)
        prev = nums[0]
        for x in range(1, len(nums)):
            if nums[x] == prev + 1:
                curr = (curr[0], nums[x])
                prev = nums[x]

            else:
                if curr[1] == -232:
                    ans.append(str(curr[0]))
                else:
                    ans.append(str(curr[0]) + "->" + str(curr[1]))
                prev = nums[x]
                curr = (nums[x], -232)

        if curr[1] == -232:
            ans.append(str(curr[0]))
        else:
            ans.append(str(curr[0]) + "->" + str(curr[1]))
        return ans
