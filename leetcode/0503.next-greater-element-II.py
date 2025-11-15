class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                idx = stack.pop()
                res[idx] = n
            stack.append(i)
        while stack:
            last_idx = stack.pop()
            for n in nums:
                if n > nums[last_idx]:
                    res[last_idx] = n
                    break
        return res
        
