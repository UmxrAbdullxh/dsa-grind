class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_map = {}
        for i,n in enumerate(nums):
            if n in duplicate_map:
                j, val = duplicate_map[n]
                diff = abs(i-j)
                if diff <= k:
                    return True
                duplicate_map[n] = (i, n)
            else:
                duplicate_map[n] = (i, n)
        return False
        