class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        ansLen = 0

        for i in range(len(s)):
            # Check the odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ansLen:
                    ans = s[l : r + 1]
                    ansLen = r - l + 1
                l -= 1
                r += 1

            # Check the even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ansLen:
                    ans = s[l : r + 1]
                    ansLen = r - l + 1
                l -= 1
                r += 1

        # ? More concise solution, less intiutive though
        # for i in range(len(s)):
        #     for j in range(2):
        #         l, r = i, i + j
        #         while l >= 0 and r < len(s) and s[l] == s[r]:
        #             if (r - l + 1) > ansLen:
        #                 ans = s[l : r + 1]
        #                 ansLen = r - l + 1
        #         l -= 1
        #         r += 1

        return ans
