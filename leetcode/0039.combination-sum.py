class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combs = []

        def dfs(i,currentSum):
            if currentSum > target or i >= len(candidates):
                return
            if currentSum == target:
                res.append(combs.copy())
                return

            combs.append(candidates[i])
            currentSum += candidates[i]
            dfs(i, currentSum)

            temp = combs.pop()
            currentSum -= candidates[i]
            dfs(i+1,currentSum)
        
        dfs(0, 0)
        return res

            
