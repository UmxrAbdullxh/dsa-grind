class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        def dfs(amount, memo):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]

            min_steps = float("inf")
            for i in range(len(coins)):
                sub = amount - coins[i]
                steps = dfs(sub, memo)
                if steps != float('inf'):
                    min_steps = min(min_steps, steps + 1)  # use one coin
            
            memo[amount] = min_steps
            return min_steps

        result = dfs(amount, {})
        return result if result != float("inf") else -1

                
        
