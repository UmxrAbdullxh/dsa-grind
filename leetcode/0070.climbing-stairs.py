class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dfs(n, {})

    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0

        res = self.dfs(n-1, memo) + self.dfs(n-2, memo)
        memo[n] = res
        return memo[n]
        
