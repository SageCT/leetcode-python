from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # * Thought Process:
        # * 1. Two pointers, one from left, one from right
        # * 2. Move the pointer with smaller height
        # * 3. Update the ans
        left = 0
        right = len(height) - 1
        toBeat: int = 0

        # ? Iterates through the entire array and updates toBeat if the current area is larger
        while left < right:
            toBeat = max(toBeat, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return toBeat
