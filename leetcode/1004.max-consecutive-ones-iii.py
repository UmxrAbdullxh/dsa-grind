class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_sum = 0
        best = 0
        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while (right-left+1)-window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            best = max(best, (right-left+1))
            right += 1
        return best
        