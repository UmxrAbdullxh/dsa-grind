class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <=nums[i] <= n:
                value = nums[i]
                target = value - 1
                if nums[target] == value:
                    break
                
                nums[i], nums[target] = nums[target], nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n+1