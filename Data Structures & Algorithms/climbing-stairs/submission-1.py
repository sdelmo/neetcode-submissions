class Solution:
    def climbStairs(self, n: int) -> int:
        """
        We want to figure out the number of distinct ways to climb to n

        Climbing 1 step means only 1 way
        Climbing 2 steps means only 2 ways
        So climbing 3 steps, is 3 (1 + 2) # Number of ways to climb a single step + 2 steps
        """
        cache = {
            1: 1,
            2: 2,
        }

        def fillcache(n):
            # Base case
            if n in cache:
                return cache[n]
            cache[n] = fillcache(n-1) + fillcache(n-2)
            return cache[n]
        
        fillcache(n)
        return cache[n]
            