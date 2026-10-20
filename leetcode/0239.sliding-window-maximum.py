class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, x in enumerate(nums):
            # kick out of window is out of window range
            if q and q[0][0] <= i - k:
                q.popleft()

            # add validation while adding if greater than right side of queue
            while q and q[-1][1] < x:
                q.pop()

            # add to q
            q.append((i, x))

            # add to res if i >=k
            if i >=k-1 :
                res.append(q[0][1])


        return res
