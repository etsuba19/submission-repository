class Solution:
    def addDigits(self, num: int) -> int:
        n = 0
        num = list(str(num))
        while len(num) > 1:
            num = sum(list(map(int, num)))
            num = list(str(num))

        return int(num[0])
