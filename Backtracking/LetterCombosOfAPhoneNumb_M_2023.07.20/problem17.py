from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # ? If length of the current string is the length
        # ? of the digits, then the answer is valid, return
        # ? Else, for each letter in the digits add the char in digitsToChar
        # ? then call backtrack() again
        def backtrack(i, curS):
            if len(curS) == len(digits):
                res.append(curS)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curS + c)

        if digits:
            backtrack(0, "")

        return res


test = "25"
print(Solution().letterCombinations(test))
