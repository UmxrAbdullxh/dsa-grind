class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-1*g for g in gifts]
        heapq.heapify(heap)
        for i in range(k):
            val = - heapq.heappop(heap)
            heapq.heappush(heap, -floor(sqrt(val)))
        return -sum(heap)
        
