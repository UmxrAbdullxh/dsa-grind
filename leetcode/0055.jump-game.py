class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Calculate farthest at any index. Update fathest max, if any index farthese < i, return false because you are stuck. If at last index, farthest < index, return true
        farthest = 0
        for i in range(len(nums)):
            if farthest < i:
                return False
            temp = i + nums[i]
            farthest = max(farthest, temp)
        return True
        
