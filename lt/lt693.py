class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last = "2"
        for i in str(bin(n))[2:]:
            if last == i:
                return False
            last = i
        return True
