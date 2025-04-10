class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        subsets = []

        hashMap = {}

        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                copy = subsets.copy()
                copyTuple = tuple(copy)
                if copyTuple not in hashMap:
                    hashMap[copyTuple] = 1
                    res.append(copy)
                return
            
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)
        
        dfs(0)
        return res
