class Solution:
    def climbStairs(self, n: int) -> int:
        # * You can use the fibbonaci sequence algo to complete this problem
        if n <= 2:
            return n

        n -= 1
        arr = []
        arr.append(1)
        arr.append(1)

        while n >= 1:
            arr.insert(0, arr[0] + arr[1])
            n -= 1
        return arr[0]
