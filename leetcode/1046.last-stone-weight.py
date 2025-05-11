class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        if len(stones) <= 0:
            return 0
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        while(len(maxHeap) > 1):
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x >= y:
                x,y = y,x
            if x != y:
                sub = y - x
                heapq.heappush(maxHeap, -sub)
        if len(maxHeap) > 0:
            return -maxHeap[0]  
        else: 
            return 0
        
