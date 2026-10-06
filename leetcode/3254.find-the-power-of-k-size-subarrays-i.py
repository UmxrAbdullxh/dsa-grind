class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1 for _ in range(n-k+1)]
        run = 1
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1] + 1:
                run += 1
            else:
                run = 1

            if i >= k-1 and run >= k:
                result[i-k+1] = nums[i] 
        return result
               