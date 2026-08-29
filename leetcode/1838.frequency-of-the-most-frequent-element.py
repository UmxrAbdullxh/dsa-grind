class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        window_sum = 0
        best = 1
        left = 0
        for right in range(len(nums)):
            window_sum += nums[right]

            # invalid conditions
            """
            to raise each element within [left, right] to nums[right], we need to perform nums[right]-nums[left] ops
            thats nums[right]-nums[left] + nums[right]-nums[left+1]..nums[right]-nums[right] times
            so each element contributes nums[right] window_len times, that is nums[right]*(right-left+1)
            remaining is nums[left] + nums[left+1]..nums[right] which is nothing but sum of window elements, so window_sum
            """
            while nums[right]*(right-left+1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            best = max(best, (right-left+1))
            right += 1
        return best
