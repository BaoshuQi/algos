class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lrgst = 0
        sl = 0
        for i in nums:
            if i > lrgst:
                sl = lrgst
                lrgst = i
            elif i > sl:
                sl = i
        if lrgst >= 2 * sl:
            return nums.index(lrgst)
        else:
            return -1