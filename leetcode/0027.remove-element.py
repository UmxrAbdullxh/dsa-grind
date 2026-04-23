class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <=r :
            if nums[l] == val and nums[r] != val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp 
                l += 1
            elif nums[l] == val and nums[r] == val:
                r -= 1
            else: 
                l += 1
        total = len(nums) - l
        while total > 0:
            nums.pop()
            total -= 1
                