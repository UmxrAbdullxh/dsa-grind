class MedianFinder:

    def __init__(self):
        # Have minHeap and maxHeap
        # Add value to maxHeap by default
        # check if all the elements in maxHeap are less or equal to all the values in maxHeap and the size difference between both heaps is at most 1
        self.maxHeap, self.minHeap = [], []
        

    def addNum(self, num: int) -> None:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        heapq.heappush(maxHeap, -1 * num)

        # check all the elements are less than or equal
        if(maxHeap and minHeap and -1 * maxHeap[0] >= minHeap[0]):
            val = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)

        # check if size is at most 1
        if(len(maxHeap) > len(minHeap)+1):
            val = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, val)
        if(len(minHeap) > len(maxHeap)+1):
            val = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -1 * val)
        

    def findMedian(self) -> float:
        maxHeap, minHeap = self.maxHeap, self.minHeap
        if(len(maxHeap) > len(minHeap)):
            return -1 * maxHeap[0]
        if(len(minHeap) > len(maxHeap)):
            return minHeap[0]
        
        return (-1*maxHeap[0] + minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
