class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height) - 1
        while ( i < j ):
            minHeight = min(height[i], height[j])
            dist = j - i
            area = dist * minHeight
            if area > res:
                res = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
        
