class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        l = 0
        maxq, minq = deque(), deque()
        for r,x in enumerate(nums):
            while maxq and maxq[-1] < x:
                maxq.pop()
            maxq.append(x)
            while minq and minq[-1] > x:
                minq.pop()
            minq.append(x)
            while (abs(maxq[0]-minq[0]) > 2):
                if nums[l] == maxq[0]:
                    maxq.popleft()
                if nums[l] == minq[0]:
                    minq.popleft()
                l += 1
            best+= (r-l+1)
        return best
