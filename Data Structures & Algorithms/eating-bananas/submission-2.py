class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        kmin, kmax = 1, max(piles)
        from math import ceil
        def timeatk(k, piles):
            hours=0
            for p in piles:
                hours += ceil(p/k)
            return hours
        
        bestk = kmax
        while kmin <= kmax:

            k = (kmin+kmax) // 2
            hrs = timeatk(k,piles)

            if hrs > h:
                kmin = k + 1
            else:
                kmax = k - 1
                bestk = k

        return bestk

            