class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
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
        
