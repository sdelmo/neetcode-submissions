class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Recursive solution
        
        cache = {
            1: 1,
            2: 2,
        }

        def fillcache(n):
            if n in cache:
                return cache[n]
            cache[n] = fillcache(n-1) + cache[n-2]
            return cache[n]
        fillcache(n)
        return cache[n]

        Uses O(n) time with the memoization
        Uses O(n) space
        """

        # Iterative, optimal for space

        a, b = 1, 1 # Ways to reach current step, 1, and ways to reach step 0 (do nothing)

        for i in range(n-1): # We only need to iterate to n-1 because n=1 already calculated
            a, b = a + b, a

        return a        
    