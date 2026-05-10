from math import sqrt
import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(p):
            x1, y1 = p # point
            x2, y2 = 0, 0 # origin

            # return euclidean distance
            return sqrt(((x1 - x2) ** 2) + ((y1-y2)**2))
        
        heap = [(dist(p), p) for p in points]
        hq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(hq.heappop(heap)[1])
        return res


    
