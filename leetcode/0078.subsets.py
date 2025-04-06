class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subsets = []
        def dfs(i):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            
            # include i
            subsets.append(nums[i])
            dfs(i+1)

            # Do not include i
            subsets.pop()
            dfs(i+1)
        
        dfs(0)
        return res
