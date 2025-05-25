class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Maintain a maxHeap with the frequencies, and a queue with the timer to

        counter = Counter(tasks)

        maxHeap = [-count for count in counter.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # Double ended queue [count, time+n]

        while maxHeap or q:
            time += 1

            # remove tasks
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time+n])
            
            if q and q[0][1] == time:
                count = q.popleft()[0]
                heapq.heappush(maxHeap, count)

        return time
        
