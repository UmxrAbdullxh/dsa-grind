class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def can_divide(threshold):
            ops = 0
            for n in nums:
                ops += math.ceil(n/threshold) - 1
                if ops > maxOperations:
                    return False
            return True

        #range
        l, r = 1, max(nums)
        while l < r:
            m = (l+r) // 2
            if can_divide(m):
                r = m
            else:
                l = m + 1
        return l
        
