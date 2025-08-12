"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval.sort()
        prev = -1;
        for i in intervals:
            if prev == -1:
                prev = i
            else:
                s1, e1 = prev[0], prev[1]
                if i[0] < e1:
                    return False
        return True 

