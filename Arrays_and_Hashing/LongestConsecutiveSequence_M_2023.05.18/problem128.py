from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        conseq: List[int] = []
        numBefore = nums[0]
        longestConseq = 1
        currConseq = 1

        for n in range(1, len(nums)):
            if nums[n] == numBefore + 1:
                conseq.append(nums[n])
                currConseq += 1
                numBefore = nums[n]
            elif nums[n] == numBefore:
                numBefore = nums[n]
            else:
                if currConseq > longestConseq:
                    longestConseq = currConseq
                currConseq = 1
                numBefore = nums[n]

        print(conseq)
        return max(longestConseq, currConseq)


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
