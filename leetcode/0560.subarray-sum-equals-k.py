class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # How do we calculate sum(i, j), Prefix?
        # sum(i, j) = sum(0, j) - sum(0, i)
        res = 0
        currSum = 0
        prefixSum = {0: 1}
        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        return res
        