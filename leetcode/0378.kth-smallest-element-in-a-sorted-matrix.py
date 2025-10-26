class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        result = []
        for list_idx, arr in enumerate(matrix):
            if arr:
                #first element, list index (which list), array pos index
                heapq.heappush(heap, (arr[0], list_idx, 0))
        
        while heap:
            val, list_idx, idx = heapq.heappop(heap)
            result.append(val)
            if idx + 1 < len(matrix[list_idx]):
                next_val = matrix[list_idx][idx+1]
                heapq.heappush(heap, (next_val,list_idx,idx+1))
        return result[k-1]

