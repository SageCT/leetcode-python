from typing import List


class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        # ? Create a list of amount + 1 values with amount + 1
        # ? Set dp[0] = 0 because it takes no coins to get to 0
        dp = [target + 1 for i in range(target + 1)]
        dp[0] = 0

        # ? For each possible coin amount (plus 0)
        # ? We will subtract the target total (a)
        # ? From the current coin amount we are testing (c)
        for a in range(1, target + 1):
            for c in coins:
                # ? If the difference of the target and the coin is greater than 0 (or equal)
                # ? You find either the target or you find the remaining difference in past calculations
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # ? If you have found a valid combo to get that target number, return dp[target]
        # ? Otherwise dp[target] == target + 1, so return -1 to indicate you can't find it
        return dp[target] if dp[target] != target + 1 else -1
