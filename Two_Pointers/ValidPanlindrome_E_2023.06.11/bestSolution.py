class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = "[\W_]+"

        import re

        n = re.sub(pattern, "", s).lower()

        return n == n[::-1]
