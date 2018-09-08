class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = [0]
        for n in w:
            self.w.append(self.w[-1] + n)
        self.s = self.w[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        import random, bisect
        r = random.random()
        p = r * self.s
        return bisect.bisect_left(self.w, p) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()