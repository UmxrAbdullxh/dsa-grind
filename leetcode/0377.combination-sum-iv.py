class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, target, {})

      
    
    def dfs(self, nums, target, memo):
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0

        res = 0

        for n in nums:
            remainder = target - n
            combSum = self.dfs(nums, remainder, memo)
            res += combSum  

        memo[target] = res
        return res
    
