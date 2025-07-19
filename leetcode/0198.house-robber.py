class Solution:
    def rob(self, nums: List[int]) -> int:

        self.max = 0

        def dfs(nums, memo):
            numsTuple = tuple(nums)
            if numsTuple in memo:
                return memo[numsTuple]
            if len(nums) < 1:
                return 0
            if len(nums) == 1:
                return nums[0]  

            total = 0
            for i in range(len(nums)):
                temp = nums[i] + dfs(nums[i+2:], memo)
                total = max(total, temp)
                if total > self.max:
                    self.max = total

            memo[tuple(nums)] = total
            return total
        
        dfs(nums, {})
        return self.max if len(nums) > 1 else nums[0]

        
