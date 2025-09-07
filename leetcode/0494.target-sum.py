class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, t, memo):
            if i >= len(nums):
                if t == target:
                    return 1
                else:
                    return 0
            if (i, t) in memo:
                return memo[(i,t)]

            memo[(i,t)] = dfs(i+1, t+nums[i], memo) + dfs(i+1, t-nums[i], memo)
            return memo[(i,t)]

        return dfs(0, 0, {})
            
