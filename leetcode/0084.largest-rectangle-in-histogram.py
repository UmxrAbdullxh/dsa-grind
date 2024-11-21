class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # contains pairs of (index, height)
        for i, h in enumerate(heights):
            # check if something in stack
            start = i
            while( stack and stack[-1][1] > h ):
                # need to pop, compute max area and push the start of the rectangle to the popped index
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))
        
        # some rectangles might be left in stack after popping, so we need to compute max area there too
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

