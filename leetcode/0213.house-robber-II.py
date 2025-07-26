class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(index, hasPicked, memo):
            if index in memo:
                return memo[index]
            if index == 0:
                if hasPicked:
                    return 0
                else:
                    return nums[0]
            if index < 0:
                return 0

            pick = nums[index] + f(index-2, hasPicked, memo)
            notPick = 0 + f(index-1, hasPicked, memo)

            res = max(pick, notPick)
            memo[index] = res
            return res
        if len(nums) == 1:
            return nums[0]
        else:
            return max(f(len(nums) - 1, True, {}), f(len(nums) -2, False, {}))
            
