from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        FoundNums = set()
        for i in nums:
            if i in FoundNums:
                return True
            FoundNums.add(i)
        return False
