class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Brute force, pick every pair and then check if equals k. 
        # TC: O(n2)
        # Sort the array and use two converging pointers?
        # TC: O(nlogn), SC:O(1)
        nums.sort()
        l, r = 0, len(nums) - 1
        max_ops = 0
        while l < r:
            nums_sum = nums[l] + nums[r]
            if  nums_sum == k:
                max_ops += 1
                l += 1
                r -= 1
            elif nums_sum < k:
                l += 1
            else:
                r -= 1
        return max_ops
        