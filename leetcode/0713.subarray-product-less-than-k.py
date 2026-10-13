class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        best = 0
        l = 0
        sub_product = 1
        for r in range(n):
            sub_product *= nums[r]
            while sub_product >= k and l < n and l <= r:
                rem = nums[l]
                sub_product = sub_product // rem
                l += 1
            best += (r-l+1)
        return best
        