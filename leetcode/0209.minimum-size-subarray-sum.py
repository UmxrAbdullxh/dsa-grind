class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        min_len = float("inf")
        i = 0
        for j in range(n):
            current_sum = prefix_sum[j] - (prefix_sum[i-1] if i > 0 else 0)
            while current_sum >= target:
                min_len = min(min_len, j - i + 1)
                i += 1
                current_sum = prefix_sum[j] - (prefix_sum[i-1] if i > 0 else 0)

        return min_len if min_len != float("inf") else 0
        