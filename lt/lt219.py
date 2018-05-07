class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        dict = {}
        for i in range (0, len(nums)):
            if i > k:
                dict.pop(nums[i - k - 1])
            if nums[i] in dict:
                return True
            dict[nums[i]] = 0
        return False
