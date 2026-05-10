class Solution:
    def climbStairs(self, n: int) -> int:
        
        # We implement this using bottom-up DP approach
        # At any given point
        # We only need steps to n-1 and n-2 to calculate steps to N

        dp = [1,2] #ways to climb 1 and 2 steps

        if n <= 2:
            return n
        
        for i in range(2, n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        
        return dp[-1]