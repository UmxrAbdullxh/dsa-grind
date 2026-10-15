class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        best = float("inf")
        running_sum = 0
        l = 0
        for r in range(n):
            running_sum += nums[r]
            while total - running_sum < x and l < n and l <= r:
                rem = nums[l]
                running_sum -= rem
                l += 1
            if total-running_sum == x:
                window_len = r-l+1
                best = min(best, n-window_len)
        if best == float("inf"):
            return -1
        return best
        