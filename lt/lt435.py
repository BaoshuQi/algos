# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        intervals.sort(key = lambda i: i.end)
        count = 1
        if not intervals:
            return 0
        cmp = intervals[0]
        for i in intervals:
            if i.start >= cmp.end:
                count += 1
                cmp = i

        return len(intervals) - count


