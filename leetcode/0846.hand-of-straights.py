class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # create counter with frequencies
        # change to list and add to minHeap
        # check if next ele is present, if not return false
        # if popping from minHeap is less than the min element, return False
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] = count[i] - 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        
