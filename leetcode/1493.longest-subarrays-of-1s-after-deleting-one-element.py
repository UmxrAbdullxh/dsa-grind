class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        best = 0
        zeroes = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            best = max(best, r-l+1)
        return best-1
        