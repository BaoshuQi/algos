"""whenever read a num from input list, find if result is in dict,
if in, return; if not, add that num to dict and continue"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for n in range (0, len(nums)):
            if nums[n] in dict:
                return [dict[nums[n]], n]
            dict[target - nums[n]] = n


print(Solution.twoSum(Solution(), [2,7,11,15], 9))