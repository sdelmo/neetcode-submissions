import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        hq.heapify(self.heap)
        self.k = k
        self.prune()

    def prune(self):
        while len(self.heap) > self.k:
            hq.heappop(self.heap)

    def add(self, val: int) -> int:
        hq.heappush(self.heap,val)
        self.prune()
        return self.heap[0]
        
