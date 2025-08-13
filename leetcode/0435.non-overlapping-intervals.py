class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the array, keep track if things are overlapping 
        # if they are overlapping, delete the one which has greater end value
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            # non overlapping case
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
        
