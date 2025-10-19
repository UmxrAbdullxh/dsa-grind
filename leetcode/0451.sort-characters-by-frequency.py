class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for n in s:
            count[n] = count.get(n, 0) - 1
        heap = [(v, k) for k, v in count.items()]
        heapq.heapify(heap)
        res = ''
        while len(heap) > 0:
            val = heapq.heappop(heap)
            for i in range(-val[0]):
                res += val[1]
        return res
        
