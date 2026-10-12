class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        best = 0
        sub_sum = 0
        l = 0
        for r in range(len(nums)):
            sub_sum += nums[r]
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            if r >= k:
                # remove
                remove = nums[l]
                sub_sum -= remove
                if freq.get(remove):
                    freq[remove] = freq.get(remove) - 1
                    if freq[remove] <= 0:
                        del freq[remove]
                l += 1
            if len(freq.keys()) == k:
                best = max(best, sub_sum)
        return best
        