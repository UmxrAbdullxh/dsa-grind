class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(a_list, low, high):
            pivot = a_list[low]
            while True:
                while a_list[low] < pivot:
                    low += 1
                while a_list[high] > pivot:
                    high -= 1
                if low >= high:
                    return high
                a_list[low], a_list[high] = a_list[high], a_list[low]
                low += 1
                high -= 1
        def _quicksort(a_list, low, high):
            if low < high: 
                p = partition(a_list, low, high)
                _quicksort(a_list, low, p)
                _quicksort(a_list, p+1, high)
        _quicksort(nums, 0, len(nums)-1)

        return nums
