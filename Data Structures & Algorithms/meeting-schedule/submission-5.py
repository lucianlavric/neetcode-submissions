"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda x: x.start)
        old_start, old_end = intervals[0].start, intervals[0].end
        for iv in intervals[1:]:
            if old_end > iv.start:
                return False
            old_end = iv.end
        return True
