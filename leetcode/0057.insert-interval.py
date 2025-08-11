class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        l, r= 0, len(intervals) - 1
        while l<=r:
            mid = (l+r)//2
            midI = intervals[mid]
            if midI[0] < newInterval[0]:
                l += 1
            else:
                r -= 1
        intervals.insert(l, newInterval)
        merge = []
        for i in range(len(intervals)):
            if i == 0:
                merge.append(intervals[i])
            else:
                last = merge[len(merge) - 1]
                present = intervals[i]
                if present[0] <= last[1]:
                    temp1 = min(present[0], last[0])
                    temp2 = max(present[1], last[1])
                    overlap = [temp1, temp2]
                    merge[len(merge) - 1] = overlap
                else:
                    merge.append(intervals[i])
        return merge
        
