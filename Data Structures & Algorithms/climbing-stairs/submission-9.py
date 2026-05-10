class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        # Bottom up dp - tabulation
        # base cases, ways to climb to 1 ways to climb to 2
        dp = [1,2]

        for n in range(2,n):
            dp[1], dp[0] = dp[0] + dp[1], dp[1]
        
        return dp[-1]