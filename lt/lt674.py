class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp = 1
        last = nums[0]
        max = 0
        for n in nums:
            if n > last:
                temp += 1
            else:
                temp = 1
            if temp > max:
                max = temp
            last = n
        return max


print(Solution.findLengthOfLCIS(Solution(),[1]))