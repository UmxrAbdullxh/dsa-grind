class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Brute force will be kind of like bubble sort where we bubble the non zero elements to the back
        TC: O(N^2). Since, nums.length is of order 10^4 this will not work
        Maintain two pointers, l and r? l always points to zero and r points to the next non zero element?
        """       
        n = len(nums)
        l = 0
        # while l < n:
        #     while l < n and nums[l] != 0:
        #         l += 1
        #     r = l
        #     while r < n and nums[r] == 0:
        #         r += 1
        #     if l < n and r < n:
        #         nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        for r in range(n):
            if l < n and nums[l] != 0:
                while l < n and nums[l] != 0:
                    l += 1
            if l < n and r < n and r >= l:
                nums[l], nums[r] = nums[r], nums[l]
                while l < n and nums[l] != 0:
                    l += 1
