class Solution:
    def jump(self, nums: List[int]) -> int:
         # Calculate farthest at any index. Update fathest max, if any index farthese < i, return false because you are stuck. If at last index, farthest < index, return true
        farthest = 0
        steps = 0
        current_end = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums) - 1):
            temp = i + nums[i]
            farthest = max(farthest, temp)
            if i == current_end:
                current_end = farthest
                steps += 1
            # if farthest >= len(nums) - 1:
            #     return steps
        return steps
        
