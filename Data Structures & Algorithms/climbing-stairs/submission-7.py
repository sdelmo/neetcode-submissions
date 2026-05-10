class Solution:
    def climbStairs(self, n: int) -> int:
        # We only need to store
        # Ways to climb n-1
        # ways to climb n
        if n <= 2:
            return n
        dp = [1, 2]

        for i in range(n-2):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        
        return dp[1]