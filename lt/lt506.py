class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {}
        r = sorted(nums)
        for i in range(0, len(nums)):
            d[r[i]] = str(len(nums) - i)
            if i == len(nums) - 1:
                d[r[i]] = "Gold Medal"
            elif i == len(nums) - 2:
                d[r[i]] = "Silver Medal"
            elif i == len(nums) - 3:
                d[r[i]] = "Bronze Medal"
        ret = []
        for n in nums:
            ret.append(d[n])
        return ret