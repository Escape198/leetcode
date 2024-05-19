class Solution:
    # dr(n) = 1 + ((n - 1) % 9)
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
