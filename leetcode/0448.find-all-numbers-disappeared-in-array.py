class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Use cyclic sort
        def cyclic_sort(arr):
            n = len(arr)
            i = 0
            while i < n:
                correct_index = arr[i]-1
                if arr[correct_index] != arr[i]:
                    arr[correct_index], arr[i] = arr[i], arr[correct_index]
                else:
                    i += 1
            return arr
        sorted_arr = cyclic_sort(nums)
        result = []
        for i in range(len(sorted_arr)):
            if sorted_arr[i]-1 != i:
                result.append(i+1)
        return result
