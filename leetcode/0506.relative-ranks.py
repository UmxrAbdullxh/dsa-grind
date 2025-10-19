class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        answer = []
        for i, n in enumerate(score):
            heap.append([-n, i])
        heapq.heapify(heap)
        answer = [""] * len(score)
        rank = 0
        while heap:
            rank += 1
            neg_sc, idx = heapq.heappop(heap)
            if rank == 1:
                answer[idx] = "Gold Medal"
            elif rank == 2:
                answer[idx] = "Silver Medal"
            elif rank == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(rank)
        return answer

