class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        return collections.Counter(nums).most_common()[-1][0]
