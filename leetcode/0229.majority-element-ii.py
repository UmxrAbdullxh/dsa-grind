class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = set()
        freq = {}
        n_arr = len(nums)
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if (freq[n] > n_arr // 3):
                res.add(n)
        return list(res)
        