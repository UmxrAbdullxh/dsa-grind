class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N, M = len(nums1), len(nums2)
        sMap = {}
        res = [-1] * N
        stack = []
        for i in range(M):
            while stack and stack[-1] <= nums2[i]:
                val = stack.pop()
                sMap[val] = nums2[i]
            stack.append(nums2[i])
        for i, n in enumerate(nums1):
            if n in sMap:
                res[i] = sMap[n]
        return res
        
