class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = min(self.dfs(0, cost, {}), self.dfs(1, cost, {}))
        return res

    def dfs(self, n, cost, memo):
        if n in memo:
            return memo[n]
        if n >= len(cost):
            return 0

        totalCost = cost[n] + min(self.dfs(n+1, cost, memo), self.dfs(n+2, cost, memo))
        memo[n] = totalCost
        return totalCost
        
