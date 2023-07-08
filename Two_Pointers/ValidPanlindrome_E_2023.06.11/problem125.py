class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isPal(word):
            return word == word[::-1]

        if len(s) == 0:
            return True
        s = "".join(i for i in s.lower() if i.isalnum() and i)

        return isPal(s)
