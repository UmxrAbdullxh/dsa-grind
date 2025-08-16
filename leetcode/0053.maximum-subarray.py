class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use Kadane's algorithm
        maxi = float("-inf")
        res = 0
        for i in nums:
            res += i

            maxi = max(res, maxi)
            
            res = max(res, 0)

        return maxi  

