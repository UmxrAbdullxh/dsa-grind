class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        result = []
        while i < n:
            correct_index = nums[i]-1
            if nums[correct_index] != nums[i]:
                nums[correct_index], nums[i] = nums[i], nums[correct_index]
            else:
                i += 1
        for i in range(n):
            if nums[i]-1 != i:
                result.append(nums[i])
        return result
        