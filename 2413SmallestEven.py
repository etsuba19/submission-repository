class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x = n
        while x >= n:
            if x % 2 == 0 and x % n == 0:
                return x
            x += 1
