class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set(nums1)
        result = set()
        for i in nums2:
            if i in intersection:
                result.add(i)
        return list(result)
        