class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n
        
        def dp(i):
            dp = [1,2]
            for i in range(n-2):
                dp[0], dp[1] = dp[1], dp[1] + dp[0]
            return dp[1]
        
        return dp(n)

        
