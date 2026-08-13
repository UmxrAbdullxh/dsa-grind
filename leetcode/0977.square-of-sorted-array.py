class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i, j = 0, len(nums) - 1
        k = len(nums) - 1
        while i <= j:
            square_1 = nums[i] ** 2
            square_2 = nums[j] ** 2
            if square_1 < square_2:
                result[k] = square_2
                j -= 1
            else:
                result[k] = square_1
                i += 1
            k -= 1
        return result
