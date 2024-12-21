from typing import List


# * Remember that this is a two pointer problem,
# * chances are you start at opposite ends of the list and iterate towards each other
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans: List[List[int]] = []

        for i in range(len(nums) - 2):
            # ? To skip over duplicates, because we sorted the list
            # ? we can check if the current number is the same as the previous number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # ? We set the left pointer to be one ahead of the current number
            # ? and the right pointer to be at the end of the list
            left = i + 1
            right = len(nums) - 1

            # ? We iterate until the left and right pointers meet
            # ? If left is greater than right, then we have checked all possible combos
            # ? For this iteration of i
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    # ? If the sum is 0, then we add the numbers to the ans list and move the pointers
                    # ? We also check if the next number is the same as the current number
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return ans
