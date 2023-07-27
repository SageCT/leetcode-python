from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checker = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in checker:
                # ? stack[-1] is the top of the stack (python is weird)
                if stack and stack[-1] == checker[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
