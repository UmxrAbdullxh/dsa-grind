class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        first_sum = sum(nums[:k]) 
        max_avg = first_sum / k
        for i in range(k, n):
            add = nums[i]
            first_sum += add
            remove = nums[i-k]
            first_sum -= remove
            avg = first_sum / k
            max_avg = max(max_avg, avg)
        return max_avg
        