class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False  # Cannot partition an odd sum equally # Cannot partition an odd sum equally

        target = total // 2

        def dfs(i, curr_sum, memo):
            if curr_sum == target:
                return True
            if i >= len(nums) or curr_sum > target:
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            include = dfs(i + 1, curr_sum + nums[i], memo)
            exclude = dfs(i + 1, curr_sum, memo)

            memo[(i, curr_sum)] = include or exclude
            return memo[(i, curr_sum)]

        return dfs(0, 0, {})
        
