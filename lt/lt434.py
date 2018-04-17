class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(list(filter(lambda w: len(w) > 0,s.split())))