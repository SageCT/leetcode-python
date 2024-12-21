from typing import List

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_num = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                min_num = min(min_num, nums[left])
                break

            mid = (left + right) // 2
            min_num = min(min_num, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return min_num
