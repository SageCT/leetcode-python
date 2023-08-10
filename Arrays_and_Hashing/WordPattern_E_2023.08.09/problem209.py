class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashT = {}
        words = s.split()
        if len(set(pattern)) == len(set(words)) and len(words) == len(list(pattern)):
            for num, i in enumerate(pattern):
                if words[num] not in hashT.values():
                    hashT[i] = words[num]
            for num, i in enumerate(pattern):
                if hashT[i] != words[num]:
                    return False
            return True
        return False


pattern = "abba"
s = "dog cat cat cat"

print(Solution().wordPattern(pattern, s))
