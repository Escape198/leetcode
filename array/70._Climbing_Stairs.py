class Solution:

    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)

        def helper(n):
            if n <= 2:
                return n

            if dp[n] is None:
                dp[n] = helper(n - 1) + helper(n - 2)
            return dp[n]

        return helper(n)
