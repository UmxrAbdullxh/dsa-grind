class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while(i<=j):
            mid = (i+j)//2
            if(nums[mid] == target):
                return mid
            #left sorted array
            if( nums[mid] >= nums[i] ):
                if nums[mid] < target or target < nums[i]:
                    i = mid + 1
                else:
                    j = mid -1 
            else:
                if nums[mid] > target or target > nums[j]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1
        
