from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        toBeat: int = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                toBeat = max(toBeat, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return toBeat
