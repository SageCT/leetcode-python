class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        c = set()
        while n > 1:
            toAdd = []
            while n > 0:
                toAdd.append(pow(n % 10, 2))
                n = n // 10
            if sum(toAdd) in c:
                return False
            elif sum(toAdd) > 1:
                c.add(sum(toAdd))
                n = sum(toAdd)
        return True
