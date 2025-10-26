class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []
        m, n = len(nums1), len(nums2)
        for i in range(min(k, m)):
            heap.append((nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        heapq.heapify(heap)
        while heap and len(res) < k:
            s, i, j, p = heapq.heappop(heap)
            res.append([i,j])
            if p+1 < n:
                heapq.heappush(heap, (i+nums2[p+1], i, nums2[p+1], p+1))
        return res
        
