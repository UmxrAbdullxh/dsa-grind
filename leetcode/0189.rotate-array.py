class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        # we need to do this if k > n
        # if k = 10, n =7, reverse k=7 will bring to the original array + 3 extra loops hence mod
        k = k % n

        def reverse(arr, i, j):
            while i < j:
                if i < n and j >= 0:
                    arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        return nums
