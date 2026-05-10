class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        heap = nums
        heapq.heapify(heap)

        # prune
        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]
