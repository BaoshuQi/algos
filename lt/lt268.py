class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return int((0 + len(nums)) * (len(nums) + 1) / 2 - sum(nums))