class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            # ? If there is a sum in the prefixSums that can add up to the difference between
            # ?  the target and the computed diff, that means it is a possible solution
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res
