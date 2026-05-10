import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heap = [-1*w for w in stones]
        hq.heapify(heap)

        while len(heap) >= 2:
            st1, st2 = -heapq.heappop(heap), -heapq.heappop(heap)

            # guaranteed that st1 should be greater than or equal, push new value in
            if st1 > st2:
                hq.heappush(heap, -(st1-st2))
        
        return 0 if not heap else -heap[0]
            





        