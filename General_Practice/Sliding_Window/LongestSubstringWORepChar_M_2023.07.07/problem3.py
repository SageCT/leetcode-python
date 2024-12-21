class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        curr_string = ""

        for c in s[::1]:
            if c not in curr_string:
                curr_string += c
                longest_string = max(longest_string, len(curr_string))
            else:
                dupe = curr_string.index(c)
                curr_string = curr_string[dupe + 1 :]
                curr_string += c

                longest_string = max(longest_string, len(curr_string))

        return longest_string
