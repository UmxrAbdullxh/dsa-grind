class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2

            leftHalf = nums[0:mid]
            rightHalf = nums[mid:]

            left = mergeSort(leftHalf)
            right = mergeSort(rightHalf)

            return merge(left, right)
        
        def merge(left, right):
            l, r = 0, 0
            result = []

            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            
            result.extend(left[l:])
            result.extend(right[r:])

            return result
        return mergeSort(nums)
        